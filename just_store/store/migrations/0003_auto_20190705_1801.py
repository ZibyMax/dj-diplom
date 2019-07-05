# Generated by Django 2.2.2 on 2019-07-05 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190705_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='parent',
            field=models.ForeignKey(default=None, limit_choices_to={'parent': None}, on_delete=django.db.models.deletion.CASCADE, to='store.Section', verbose_name='Родительский раздел'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Раздел'),
        ),
        migrations.DeleteModel(
            name='MainSection',
        ),
    ]
