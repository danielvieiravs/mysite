from django.contrib import admin
from daterange_filter.filter import DateRangeFilter

from import_export.admin import ImportExportModelAdmin

from .models import Flat, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class FlatAdmin(ImportExportModelAdmin):
    list_display = ('date_to_rent', 'licensor', 'property', 'area',
                    'number_bedrooms', 'price_one', 'price_two', 'post_code')
    list_filter = ( ('date_to_rent', DateRangeFilter), 'licensor', 'property',
                   'area', 'price_one', 'price_two', 'post_code',
                   'number_bedrooms',)
    search_fields = ('licensor', 'property', 'area', 'number_bedrooms',
                     'price_one', 'price_two', 'post_code')
    inlines = [
        PhotoInline,
    ]


admin.site.register(Flat, FlatAdmin)