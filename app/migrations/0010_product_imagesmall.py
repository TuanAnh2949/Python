# Generated by Django 4.2 on 2023-05-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_product_imagesmall'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagesmall',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
