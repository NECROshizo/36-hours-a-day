from django.contrib import admin

from .models import Dialer, DealerPrice, Product, ProductDialerKey


@admin.register(Dialer)
class DialerAdmin(admin.ModelAdmin):
    """Админка для дилера."""

    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для товаров заказчика."""

    list_display = (
        'id',
        "article",
        "ean_13",
        "name",
        "cost",
        "min_recommended_price",
        "recommended_price",
        "category_id",
        "ozon_name",
        "name_1c",
        "wb_name",
        "ozon_article",
        "wb_article",
        "ym_article",
        "wb_article_td",
    )
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(DealerPrice)
class DealerPriceAdmin(admin.ModelAdmin):
    """Админка товаров дилера."""

    list_display = (
        'id',
        "product_key",
        "price",
        "product_url",
        "product_name",
        "date",
        "dealer_id",
    )
    list_filter = ("product_name",)
    empty_value_display = "-пусто-"


@admin.register(ProductDialerKey)
class ProductDialerKeyAdmin(admin.ModelAdmin):
    """Связка товаров."""

    list_display = (
        "id",
        "product_key",
        "product_id",
    )
    empty_value_display = "-пусто-"
