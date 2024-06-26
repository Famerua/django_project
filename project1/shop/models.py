from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(null=False, max_length=255, default="")
    desription = models.CharField(null=False, max_length=3000, default="")
    price = models.IntegerField(null=False, default=0)
    amount = models.IntegerField(null=False, default=0)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"ID: {self.id}, NAME: {self.name}"
