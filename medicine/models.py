from django.db import models


class Inventory(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id', 'sku_id', 'product_id', 'sku_name'], name="unique_keys")
        ]

    id = models.AutoField(primary_key=True)
    sku_id = models.FloatField(max_length=200, null=True)
    product_id = models.FloatField(max_length=200, null=True)
    sku_name = models.CharField(max_length=200, default='-')
    price = models.FloatField(max_length=50, default=None)
    manufacturer_name = models.CharField(max_length=200, default='-')
    salt_name = models.CharField(max_length=200, default='-')
    drug_form = models.CharField(max_length=50, default='-')
    pack_size = models.CharField(max_length=100, default='-')
    strength = models.CharField(max_length=200, null=True)
    product_banned_flag = models.BooleanField(null=True, default=False)
    unit = models.CharField(max_length=50, null=True)
    price_per_unit = models.FloatField(max_length=200, null=True)
