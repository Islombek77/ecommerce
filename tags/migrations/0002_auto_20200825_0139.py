# Generated by Django 3.1 on 2020-08-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_slug'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='active',
        ),
        migrations.AddField(
            model_name='tag',
            name='active',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
