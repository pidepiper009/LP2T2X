# Generated by Django 3.2.6 on 2021-10-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211014_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.CharField(max_length=120),
        ),
    ]
