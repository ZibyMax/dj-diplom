from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    registration_date = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    @property
    def show_money_count(self):
        money_count = 0
        for order in Order.objects.filter(user=self).prefetch_related('products'):
            for order_line in order.products.all():
                money_count += order_line.product.price * order_line.quantity
        return money_count


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='Раздел')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Категория')
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['order']


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    picture = models.CharField(max_length=100, verbose_name='Изображение')
    description = models.CharField(max_length=200, verbose_name='Описание')
    section = models.ForeignKey(Section, verbose_name='Раздел', on_delete=models.CASCADE)
    order = models.IntegerField(default=0, verbose_name='Порядок')
    price = models.FloatField(default=0, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['order']


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст статьи')
    products = models.ManyToManyField(Product, verbose_name='Связанные товары')
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['order']


class OrderLine(models.Model):
    product = models.ForeignKey(Product, verbose_name='Наименование товара', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество товара')

    def __str__(self):
        return f'{self.product.title} - {self.quantity}pcs.'

    class Meta:
        verbose_name = 'Строка заказа'
        verbose_name_plural = 'Строки заказа'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Заказчик', on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderLine, verbose_name='Строки заказа')

    def __str__(self):
        return f'Заказ {self.pk} - {self.user.username}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

