from django.conf.urls import include, url
from django.contrib import admin

from shipping.models import Shipping
from shipping.viewsets import ShippingViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'shipping', ShippingViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'marvexbe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
