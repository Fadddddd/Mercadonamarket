# Generated by Django 4.2.5 on 2023-12-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_rename_description_product_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descriptions',
            new_name='description',
        ),
    ]