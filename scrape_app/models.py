from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_source = models.CharField(max_length=20)
    product_price = models.CharField(max_length=20)
    product_image_link = models.CharField(max_length=255)
    product_link = models.CharField(max_length=255)
    adddate = models.DateTimeField(db_column='ADDDATE', auto_now_add=True)  

    def __str__(self):
        return "%s - %s" % (self.product_source, self.product_name)