# Generated by Django 3.1.5 on 2021-01-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_auto_20210126_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='catalogue',
        ),
        migrations.AddField(
            model_name='inventory',
            name='drug_form',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='inventory',
            name='manufacturer_name',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='inventory',
            name='pack_size',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='inventory',
            name='price',
            field=models.FloatField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_banned_flag',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_id',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='salt_name',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='inventory',
            name='sku_id',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='sku_name',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='inventory',
            name='strength',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.UniqueConstraint(fields=('id', 'sku_id', 'product_id', 'sku_name'), name='unique_keys'),
        ),
        migrations.DeleteModel(
            name='Catalogue',
        ),
    ]
