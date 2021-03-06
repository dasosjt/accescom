# Generated by Django 3.1.2 on 2020-11-12 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=255, unique=True)),
                ('units', models.IntegerField()),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.shoppingcart')),
            ],
        ),
    ]
