# Generated by Django 4.2 on 2023-05-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagesmall',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
