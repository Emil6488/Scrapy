# Generated by Django 3.2.8 on 2021-11-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0002_auto_20211104_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='userId',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
