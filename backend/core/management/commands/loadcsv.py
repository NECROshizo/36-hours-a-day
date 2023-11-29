import csv
import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from product.models import Dialer, Product


def create_dialer_model(file_data: csv.DictReader):
    """Создание простой модели."""
    Dialer.objects.all().delete()
    Dialer.objects.bulk_create(
        [
            Dialer(**row)
            for row in file_data
        ]
    )


def create_product_model(file_data: csv.DictReader):
    """Создание модели Product."""
    Product.objects.all().delete()
    # Product.objects.bulk_create(
    #     [
    #         Product(
    #             id=row.get('id'),
    #             article=row.get('article'),
    #             ean_13=int(float(row.get('ean_13', 0))),
    #             name=row.get('name'),
    #             cost=float(row.get('cost')) #decimal.Decimal(str(row.get('cost'))),
    #             # text=row.get('text'),
    #             # cooking_time=row.get('cooking_time')
    #         )
    #         for row in file_data
    #     ]
    # )
    for row in file_data:
        value = row.get('ean_13', 0)
        print(value)
        #print(type(value))


class Command(BaseCommand):
    help = 'Загрузка данных из CSV файлов'
    link_models = (
        ('marketing_dealer.csv', create_dialer_model),
        ('marketing_product.csv', create_product_model),
    )

    def handle(self, *args, **options):
        work_dir = Path(Path(settings.BASE_DIR).parent, 'data')
        with os.scandir(work_dir) as files:
            files = [file.name for file in files if file.is_file()
                     and file.name.endswith('.csv')]

        print('загрузка данных из файла(ов):')

        # будем грузить по порядку иначе будут проблемы
        for file, func in self.link_models:
            if file in files:
                with open(Path(work_dir, file), encoding='utf-8') as h_file:
                    file_reader = csv.DictReader(h_file, delimiter=';')
                    print(f'{file} - ', end='')
                    try:
                        func(file_reader)
                        print('\033[32m OK \033[0;0m')
                    except Exception as err:
                        print(err)
                        print('\033[31m NO \033[0;0m')
            else:
                print(f'{file} - \033[31m NO \033[0;0m')