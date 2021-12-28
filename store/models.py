from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    main_inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email= models.EmailField(unique = True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    # class Meta:
        # db_table = 'store_customers'
        # indexes = [
            # models.Index(fields=['last_name','first_name'])
        # ]

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField('Customer', on_delete=CASCADE, primary_key=True)

