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
    # dealer_name = serializers.StringRelatedField(
    #     many=False,
    #     read_only=True
    # )

    dealer = DialerSerializer(
        many=False
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
            'is_defined',       # привязка присутсвует
        )             

    def get_is_defined(self, obj):    # TODO: Реализовать метод 
        return True                     


