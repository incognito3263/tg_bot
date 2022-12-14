# Generated by Django 4.0.4 on 2022-04-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_collection_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserChatId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=500, verbose_name='ID пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
