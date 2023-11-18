# Generated by Django 4.2.5 on 2023-11-18 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='')),
                ('categorie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchandise.product')),
            ],
        ),
    ]
