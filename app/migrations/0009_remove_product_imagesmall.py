# Generated by Django 4.2 on 2023-05-25 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_imagesmall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imagesmall',
        ),
    ]
