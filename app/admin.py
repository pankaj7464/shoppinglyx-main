from django.contrib import admin
from .models import (Customer,Product,Cart,OrderPlace)

# Register your models here.
@admin.register(Customer)
class CostomerModeladmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModeladmin(admin.ModelAdmin):
    list_display=['id','tittle','selling_price','discounted_price','discription','brand','category']

@admin.register(Cart)
class CartModeladmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlace)
class OrderModeladmin(admin.ModelAdmin):
    list_display = ['id','user','product','customer','quantity','ordered_date','status']