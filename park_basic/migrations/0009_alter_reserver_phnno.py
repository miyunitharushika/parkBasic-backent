# Generated by Django 5.0.1 on 2024-01-03 10:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park_basic', '0008_alter_reserver_carno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserver',
            name='phnNo',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Enter a valid Sri Lankan phone number.', regex='^(?:7|0|(?:\\+94))[0-9]{9,10}$')]),
        ),
    ]
