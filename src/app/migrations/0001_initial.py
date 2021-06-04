# Generated by Django 3.2.3 on 2021-05-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Файл')),
                ('image_link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('image_resized', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Измененный файл')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота')),
            ],
        ),
    ]