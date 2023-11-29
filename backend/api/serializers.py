from rest_framework import serializers

from product.models import Dialer, DealerPrice

class DialerSerializer(serializers.ModelSerializer):
    """Сериализатор для дилера."""
    class Meta:
        model = Dialer
        fields = (
            'id',
            'name',
        )

class DialerPriceSerializer(serializers.ModelSerializer):    
    """Сериализатор продукции дилера."""
    dealer_name = serializers.StringRelatedField(
        many=False,
        read_only=True
    )

    is_defined = serializers.SerializerMethodField()

    class Meta:
        model = DealerPrice
        fields = (
            'id',
            'product_key',
            'price', 
            'product_url',
            'product_name', 
            'date', 
            'dealer_id',
            'dealer_name',
        )             

    def get_is_favorited(self, obj):
        return True
