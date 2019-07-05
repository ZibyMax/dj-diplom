from django.db import models


class MainSection(models.Model):
    title = models.CharField(max_length=100, verbose_name='Основной раздел')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='Дополнительный раздел')
    parent = models.ForeignKey(MainSection, null=False, verbose_name='Родительский раздел', on_delete=models.CASCADE)

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

