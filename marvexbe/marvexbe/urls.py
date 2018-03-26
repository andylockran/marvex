from django.conf.urls import include, url
from django.contrib import admin

from shipping.models import Shipping
from shipping.viewsets import ShippingViewSet

from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'shipping', ShippingViewSet)

schema_view = get_swagger_view(title='Marine Vexillology')

urlpatterns = [
    # Examples:
    # url(r'^$', 'marvexbe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^swagger/', schema_view),
    url(r'^docs/', include_docs_urls(title='Marine Vexillology'))
]
