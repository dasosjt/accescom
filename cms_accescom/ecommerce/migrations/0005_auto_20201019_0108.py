# Generated by Django 3.1.2 on 2020-10-19 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20201013_0310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='coin_type',
            new_name='product_coin_type',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unit_type',
            new_name='product_unit_type',
        ),
    ]
