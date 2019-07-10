from django.contrib import admin
from .models import Category, Section, Product, Article


class CategoryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'description', 'section')


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)

admin.site.register(Section, SectionAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Article, ArticleAdmin)

