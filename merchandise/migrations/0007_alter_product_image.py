# Generated by Django 4.2.5 on 2023-12-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0006_remove_product_categories_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
