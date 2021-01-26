# Generated by Django 3.1.5 on 2021-01-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_auto_20210126_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='drug_form',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='pack_size',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='salt_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]