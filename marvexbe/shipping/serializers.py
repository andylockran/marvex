from rest_framework import serializers
from shipping.models import Shipping

class ShippingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shipping
        fields = (
            'fk_id', 
            'company_name', 
            'alternative_name',
            'managers',
            'manager_names',
            'date_founded',
            'date_ceased',
            'cessation_field',
            'remarks',
            'provenance',
            'registered', 
            'nationality',
            'category',
            'jll_sighted'
        )
