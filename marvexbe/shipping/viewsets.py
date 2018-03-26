from rest_framework import viewsets
from rest_framework.response import Response
from shipping.models import Shipping
from django_filters.rest_framework import DjangoFilterBackend

from shipping.serializers import ShippingSerializer


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('registered', 'jll_sighted', 'nationality')

