from rest_framework import serializers
from shipping.models import Shipping

class ShippingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shipping
        fields = ('fk_id', 'company_na', 'registered', 'nationalit')
