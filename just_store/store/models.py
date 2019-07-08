from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='Раздел')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Категория')
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    picture = models.CharField(max_length=100, verbose_name='Изображение')
    description = models.CharField(max_length=200, verbose_name='Описание')
    section = models.ForeignKey(Section, verbose_name='Раздел', on_delete=models.CASCADE)
    order = models.IntegerField(default=0, verbose_name='Порядок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

