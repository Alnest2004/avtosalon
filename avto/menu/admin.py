from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CarsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("model",)}
    list_display = ['model', 'slug', 'short_text','get_html_photo', 'time_create']
    list_filter = ['time_create', 'cat']
    list_per_page = 5
    ordering = ['model', ]



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']


admin.site.register(Cars, CarsAdmin)
admin.site.register(Category, CategoryAdmin)
