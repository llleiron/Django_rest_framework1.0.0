# Generated by Django 2.0.12 on 2020-03-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_order_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_by',
        ),
    ]
