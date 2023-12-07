import csv
import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from product.models import Dialer, DealerPrice, MLResult, Product, ProductDialerKey


def get_int_value_from_row(row, name):
    return 0 if row.get(name, 0) == "" else int(float(row.get(name, 0)))


def get_float_value_from_row(row, name):
    return float(0 if row.get(name, 0) == "" else row.get(name, 0))


def get_dialer_obj(row, name):
    if Dialer.objects.filter(id=row.get(name)).exists():
        return Dialer.objects.get(id=row.get(name))


def get_product_obj(row, name):
    if Product.objects.filter(id=row.get(name)).exists():
        return Product.objects.get(id=row.get(name))


def create_dialer_model(file_data: csv.DictReader):
    """Создание простой модели."""
    Dialer.objects.all().delete()
    Dialer.objects.bulk_create([Dialer(**row) for row in file_data])


def create_product_model(file_data: csv.DictReader):
    """Создание модели Product."""
    Product.objects.all().delete()
    Product.objects.bulk_create(
        [
            Product(
                id=row.get("id"),
                article=row.get("article"),
                ean_13=get_int_value_from_row(row, "ean_13"),
                name=row.get("name"),
                cost=get_float_value_from_row(row, "cost"),
                min_recommended_price=get_float_value_from_row(
                    row, "min_recommended_price"
                ),
                recommended_price=get_float_value_from_row(row, "recommended_price"),
                category_id=get_int_value_from_row(row, "category_id"),
                ozon_name=row.get("ozon_name"),
                name_1c=row.get("name_1c"),
                wb_name=row.get("wb_name"),
                ozon_article=row.get("ozon_article"),
                wb_article=row.get("wb_article"),
                ym_article=row.get("ym_article"),
                wb_article_td=row.get("wb_article_td"),
            )
            for row in file_data
        ]
    )


def create_dealerprice_model(file_data: csv.DictReader):
    """Создание модели Product."""
    DealerPrice.objects.all().delete()
    DealerPrice.objects.bulk_create(
        [
            DealerPrice(
                id=row.get("id"),
                product_key=row.get("product_key"),
                price=get_float_value_from_row(row, "price"),
                product_url=row.get("product_url", ""),
                product_name=row.get("product_name"),
                date=row.get("date"),
                dealer_id=get_dialer_obj(row, 'dealer_id'),
            )
            for row in file_data
            if get_dialer_obj(row, 'dealer_id')
        ]
    )


def create_product_dialer_model(file_data: csv.DictReader):
    ProductDialerKey.objects.all().delete()
    ProductDialerKey.objects.bulk_create(
        [
            ProductDialerKey(
                id=row.get("id"),
                product_key=row.get("key"),
                product_id=get_product_obj(row, 'product_id')
            )
            for row in file_data
            if get_product_obj(row, 'product_id')
        ]
    )


def create_ml_model(file_data: csv.DictReader):
    MLResult.objects.all().delete()
    MLResult.objects.bulk_create(
        [
            MLResult(
                id=row.get("id"),
                product_key=row.get("key"),
                product_id=get_product_obj(row, 'product_id')
            )
            for row in file_data
            if get_product_obj(row, 'product_id')
        ]
    )


class Command(BaseCommand):
    help = "Загрузка данных из CSV файлов"
    link_models = (
        ("marketing_dealer.csv", create_dialer_model),
        ("marketing_product.csv", create_product_model),
        ("marketing_dealerprice.csv", create_dealerprice_model),
        ('marketing_productdealerkey.csv', create_product_dialer_model),
        ('ml_result.csv', create_ml_model),
    )

    def handle(self, *args, **options):
        work_dir = Path(Path(settings.BASE_DIR).parent, "data")
        with os.scandir(work_dir) as files:
            files = [
                file.name
                for file in files
                if file.is_file() and file.name.endswith(".csv")
            ]

        print("загрузка данных из файла(ов):")

        # будем грузить по порядку иначе будут проблемы
        for file, func in self.link_models:
            if file in files:
                with open(Path(work_dir, file), encoding="utf-8") as h_file:
                    file_reader = csv.DictReader(h_file, delimiter=";")
                    print(f"{file} - ", end="")
                    try:
                        func(file_reader)
                        print("\033[32m OK \033[0;0m")
                    except Exception as err:
                        print(err)
                        print("\033[31m NO \033[0;0m")
            else:
                print(f"{file} - \033[31m NO \033[0;0m")
