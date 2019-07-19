from django.contrib import admin
from .models import User, Category, Section, Product, Article, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'registration_date']


class CategoryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'description', 'section')


class ArticleAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Section, SectionAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Article, ArticleAdmin)

admin.site.register(Order, OrderAdmin)

