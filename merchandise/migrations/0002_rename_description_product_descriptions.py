# Generated by Django 4.2.5 on 2023-12-25 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='descriptions',
        ),
    ]
