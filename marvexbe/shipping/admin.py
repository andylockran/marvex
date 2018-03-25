# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from import_export import resources
from shipping.models import Shipping

from import_export.admin import ImportExportModelAdmin



class ShippingResource(resources.ModelResource):

    class Meta:
        model = Shipping

#class ShippingAdmin(ImportExportModelAdmin):
#    resource_class = ShippingResource

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('fk_id', 'company_name', 'registered')
    list_filter = ('date_founded', 'date_ceased')


admin.site.register(Shipping, ShippingAdmin);