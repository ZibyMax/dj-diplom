from django.contrib import admin
from .models import Section, Product


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'description', 'section')


admin.site.register(Section, SectionAdmin)

admin.site.register(Product, ProductAdmin)