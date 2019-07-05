from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='Раздел')
    parent = models.ForeignKey('self', default=None, verbose_name='Родительский раздел', on_delete=models.CASCADE,
                               limit_choices_to={'parent': None})

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

