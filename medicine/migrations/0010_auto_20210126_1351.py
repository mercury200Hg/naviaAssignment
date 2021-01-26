# Generated by Django 3.1.5 on 2021-01-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0009_auto_20210126_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='drug_form',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='pack_size',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='salt_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='sku_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AddConstraint(
            model_name='catalogue',
            constraint=models.UniqueConstraint(fields=('id', 'sku_id', 'product_id', 'sku_name'), name='unique_keys'),
        ),
    ]