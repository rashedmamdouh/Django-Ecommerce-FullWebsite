# Generated by Django 4.2.1 on 2023-06-24 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_cart_prod_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
