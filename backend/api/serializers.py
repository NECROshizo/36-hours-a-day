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
    dealer = DialerSerializer(
        many=False,
        read_only=True,
        source='dealer_id'
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
            'dealer',
            'is_defined',      
        )             

    def get_is_defined(self, obj):     
        return obj.product_link.exists()                     


