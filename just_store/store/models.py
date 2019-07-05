from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100, verbose_name='Раздел')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name='Родительский раздел')

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

