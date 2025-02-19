from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Django сам управляет ID
    product = models.CharField(max_length=200)
    type = models.CharField(max_length=3)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.product
