# Generated by Django 2.0.12 on 2020-03-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20200302_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('YE', 'Yndunvac e'), ('YD', 'Yndunel e'), ('BE', 'Berum e')], max_length=3, null=True, verbose_name='Status'),
        ),
    ]
