from django.shortcuts import render
from django.views import View
from .models import Customer,Cart,Product,OrderPlace
from .forms import CustomerResistrationForm ,CustomerProfileForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='tw')
        bottonwears = Product.objects.filter(category='bw')
        mobiles = Product.objects.filter(category='m')
        laptop = Product.objects.filter(category='l')
        context = {'topwears': topwears,'bottonwears' :bottonwears,'mobiles':mobiles,'laptop':laptop}
        return render(request, 'app/home.html',context)


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self,request,pk):
        productview = Product.objects.get(pk = pk)
        return render(request, 'app/productdetail.html',{'productview':productview})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data = None):
    if data == None:
        mobile = Product.objects.filter(category='m')
    elif data == 'samsung' or data =='redmi':
        mobile = Product.objects.filter(category='m').filter(brand= data)
    elif data == 'bellow':
        mobile = Product.objects.filter(category='m').filter(discounted_price__lt = 10000)
    elif data == 'above':
        mobile = Product.objects.filter(category='m').filter(discounted_price__gt = 10000)
    return render(request, 'app/mobile.html',{'mobile':mobile})

class CustomerResistrationView(View):
    def get(self,request):
        form = CustomerResistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerResistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Resistered Successfully...')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})
    



def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            
            form.save()
        return render(request, 'app/profile.html',{'form':form})