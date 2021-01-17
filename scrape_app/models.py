from django.db import models

# Create your models here.

class ProductSource(models.Model):
    product_source = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % (self.product_source)


class ProductType(models.Model):
    product_type = models.CharField(max_length=30)

    def __str__(self):
        return "%s" % (self.product_type)


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    product_source = models.ForeignKey(ProductSource, on_delete=models.CASCADE)
    product_price = models.CharField(max_length=20)
    product_image_link = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)
    adddate = models.DateTimeField(db_column='ADDDATE', auto_now_add=True)  
    editdate = models.DateTimeField(db_column='EDITDATE', auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.product_source, self.product_name)