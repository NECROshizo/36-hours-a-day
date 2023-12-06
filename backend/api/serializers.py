from rest_framework import serializers

from product.models import Dialer, DealerPrice, Product, ProductDialerKey, MLResult


class ShortProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
        )


class DialerSerializer(serializers.ModelSerializer):
    """Сериализатор для дилера."""

    class Meta:
        model = Dialer
        fields = (
            "id",
            "name",
        )


class DialerPriceSerializer(serializers.ModelSerializer):
    """Сериализатор продукции дилера."""

    dealer = DialerSerializer(many=False, read_only=True, source="dealer_id")

    is_defined = serializers.SerializerMethodField()
    product_cust = serializers.SerializerMethodField()

    class Meta:
        model = DealerPrice
        fields = (
            "product_key",
            "price",
            "product_url",
            "product_name",
            "date",
            "dealer",
            "is_defined",
            "product_cust",
        )

    def get_is_defined(self, obj):
        return ProductDialerKey.objects.filter(product_key=obj.product_key).exists()

    def get_product_cust(self, obj):
        if ProductDialerKey.objects.filter(product_key=obj.product_key).exists():
            instance = ProductDialerKey.objects.filter(product_key=obj.product_key)[0]
            return ShortProductSerializer(instance.product_id).data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
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


class DialerPriceDSSerializer(serializers.ModelSerializer):
    """Сериализатор продукции дилера для DS."""

    class Meta:
        model = DealerPrice
        fields = (
            "id",
            "product_key",
            "price",
            "product_url",
            "product_name",
            "date",
            "dealer_id",
        )

class MLResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLResult
        fields = (
            "product_key",
            "product_id",
        )
