from django.db import models
from django.db.models import UniqueConstraint


class Dialer(models.Model):
    """Список дилеров."""

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Дилер"
        verbose_name_plural = "Дилеры"


class Product(models.Model):
    """Продукция заказчика."""

    article = models.CharField(max_length=30)
    ean_13 = models.IntegerField()
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=13, decimal_places=2)
    min_recommended_price = models.DecimalField(max_digits=13, decimal_places=2)
    recommended_price = models.DecimalField(max_digits=13, decimal_places=2)
    category_id = models.IntegerField()
    ozon_name = models.CharField(max_length=255)
    name_1c = models.CharField(max_length=255)
    wb_name = models.CharField(max_length=255)
    ozon_article = models.TextField()
    wb_article = models.TextField()
    ym_article = models.TextField()
    wb_article_td = models.TextField()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class DealerPrice(models.Model):
    """Данные дилера."""

    product_key = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    product_url = models.TextField()
    product_name = models.CharField(max_length=255)
    date = models.DateField()
    dealer_id = models.ForeignKey(
        Dialer, on_delete=models.CASCADE, related_name="dialer_prices"
    )

    class Meta:
        verbose_name = "Товар дилера"
        verbose_name_plural = "Товары дилера"


class ProductDialerKey(models.Model):
    """Связка."""

    product_key = models.ForeignKey(
        DealerPrice, on_delete=models.CASCADE, related_name="product_link"
    )
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_link"
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=["product_key", "product_id"], name="product link")
        ]
        verbose_name = "Связка"
        verbose_name_plural = "Связки"
