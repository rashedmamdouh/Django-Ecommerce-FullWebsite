# Generated by Django 4.2.1 on 2023-06-24 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_remove_orders_product_delete_selledproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]