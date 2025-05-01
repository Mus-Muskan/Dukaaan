from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    '''Specifies that when the associated User instance is deleted, 
        the related instance of your model should also be automatically deleted.
      This ensures referential integrity by preventing orphaned records.'''
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def  __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital_product = models.BooleanField(default=False, null=True, blank=True)
    '''stores info: Does the product need to be shipped? Or if its only digitally available'''
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    placed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null = True)

    def __str__(self):
        return str(self.id)
    
class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quatity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
    
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address