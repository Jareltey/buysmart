# Generated by Django 3.0.3 on 2020-04-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20200422_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='price',
            field=models.FloatField(default=''),
        ),
    ]
