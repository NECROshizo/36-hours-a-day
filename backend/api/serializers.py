from rest_framework import serializers

from product.models import Dialer, DealerPrice, Product


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
            "id",
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
        return obj.product_link.exists()

    def get_product_cust(self, obj):
        if obj.product_link.exists():
            instance = obj.product_link.all()[0].product_id
            return ShortProductSerializer(instance).data


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
