import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pymorphy2

import warnings
warnings.filterwarnings('ignore')

# количество выводимых рекомендаций
K = 5

def matching(dealer_json: list, products_json: list):
    
    if isinstance(products_json, list):
        data_products = pd.DataFrame(products_json)
    if isinstance(dealer_json, list):
        data_dealers = pd.DataFrame(dealer_json)

    # подготовка датасетов
    # удалить продукты дубликаты, спарсенные в разные дни
    data_dealers = data_dealers[~data_dealers.drop(['id', 'date'], axis=1).duplicated(keep='first')]

    # удалить пропуски в столбце с именем
    data_products = data_products.dropna(subset=['name'])
    # заменить вручную ошибки, которые не обработаются функцией
    data_products['name'] = data_products['name'].str.replace('C редство', 'Средство')
    data_products['name'] = data_products['name'].str.replace('БЕТОНКОНТАКТготовый', 'БЕТОНКОНТАКТ готовый')
    data_products['name'] = data_products['name'].str.replace('"к', '" к')
    data_products['name'] = data_products['name'].str.replace('яблокаконцентрированное', 'яблока концентрированное')
    data_products['name'] = data_products['name'].str.replace('(сухой остаток 20%)', ' (сухой остаток 20%) ')
    data_products['name'] = data_products['name'].str.replace('.C', '. C')

    def add_spaces(data):
        # Добавляет пробелы 
        spaced_text = re.sub(r'(?<=[a-zA-Z])(?=[а-яА-ЯёЁ])|(?<=[а-яА-ЯёЁ])(?=[a-zA-Z])', ' ', data)
        spaced_text = re.sub(r'(\S)\*(\S)', r'\1 * \2', spaced_text)
        spaced_text = re.sub(r'(\d+)([а-яА-ЯёЁa-zA-Z]+)', r'\1 \2', spaced_text)
        return spaced_text

    # Функция очистки,  токенизации, лемматизации и удаление стоп-слов.
    def preprocess_text(text):
        # Очистка текста
        cleaned_text = re.sub(r"[^a-zA-Zа-яА-ЯёЁ 0-9,.:]", ' ', text)
        cleaned_text = re.sub(r"[,]", '', cleaned_text)

        # Токенизация
        tokens = word_tokenize(cleaned_text.lower())

        morph = pymorphy2.MorphAnalyzer()
        lemmas = [morph.parse(word)[0][2] for word in tokens]

        # Удаление стоп-слов
        stop_words = set(stopwords.words('russian') + stopwords.words('english'))
        filtered_words = [lemma for lemma in lemmas if lemma not in stop_words]

        # Возвращение предобработанного текста
        return ' '.join(filtered_words)
    
    # обработка текста
    data_products['name_clean'] = data_products['name'].apply(
        lambda x: preprocess_text(add_spaces(x))
        )
    data_dealers['product_name_clean'] = data_dealers['product_name'].apply(
        lambda x: preprocess_text(add_spaces(x))
        )

    vectorizer = TfidfVectorizer()

    # эмбединги
    product_tfidf_matrix = vectorizer.fit_transform(data_products['name_clean'].tolist())
    dealers_tfidf_matrix = vectorizer.transform(data_dealers['product_name_clean'].tolist())
    
    # рассчитываем сходство
    cosine_similarities = cosine_similarity(dealers_tfidf_matrix, product_tfidf_matrix)

    # Индексы 5 наиболее близких объектов для каждого дилера
    top_n_indices = np.argsort(cosine_similarities, axis=1)[:, ::-1][:, :K]

    # создаем список словарей для хранения результатов
    result_list = []

    # итерируемся по каждому дилеру
    for i, dealer_row in enumerate(top_n_indices):
        dealer_key = data_dealers.iloc[i]['product_key']

        # итерируемся по топовым индексам
        for j in dealer_row:
            product_id = data_products.iloc[j]['id']

            # добавляем пару в список
            result_list.append({'product_key': dealer_key, 'product_id': product_id})

    return result_list