from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATE_CHOICES = (('Bihar', 'Bihar'), ('Panjab', 'Panjab'),
                 ('Gujarat', 'Gujarat'))


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=30)

    def __str__(self):
        return str(self.id)


CATEGOTY_CHOICES = (('m', 'mobile'), ('l', 'laptop'),
                    ('tp', 'top wear'), ('bt', 'botton wear'))


class Product(models.Model):
    tittle = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGOTY_CHOICES, max_length=2)
    producat_image = models.ImageField(upload_to='product_img')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (('accepted', 'accepted'), ('packed', 'packed'), ('on the way',
                  'on the way'), ('delivered', 'delivered'), ('cancel', 'cancel'))

class OrderPlace(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    quantity = models.IntegerField(default = 1)
    ordered_date  = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    def __str__(self):
        return str(self.id)