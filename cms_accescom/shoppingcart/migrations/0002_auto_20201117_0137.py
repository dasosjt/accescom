# Generated by Django 3.1.2 on 2020-11-17 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='sku',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]