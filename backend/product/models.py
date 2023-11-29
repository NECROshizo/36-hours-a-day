from django.db import models

class Dialer(models.Model):
    """Список дилеров.""" 
    name = models.CharField(max_length=100)


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
     

class DealerPrice(models.Model):
    """Данные дилера."""

    product_key = models.CharField(primary_key=True, max_length=255)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    product_url = models.TextField()
    product_name = models.CharField(max_length=255)
    date = models.DateField() 
    dealer_id = models.ForeignKey(
        Dialer,
        on_delete=models.CASCADE,
        related_name='dialer_prices'
    ) 

class ProductDialerKey(models.Model):
    """Связка."""

    product_key = models.ForeignKey(
        DealerPrice,
        on_delete=models.CASCADE,
        related_name='product_link'
    ) 
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_link'
    )
