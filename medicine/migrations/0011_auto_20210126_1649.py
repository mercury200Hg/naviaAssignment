# Generated by Django 3.1.5 on 2021-01-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0010_auto_20210126_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='catalogue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogue', to='medicine.catalogue'),
        ),
    ]