# Generated by Django 4.0.4 on 2022-04-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_collection_created_collection_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Комментарий'),
        ),
    ]
