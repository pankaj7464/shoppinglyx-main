from django.shortcuts import render ,redirect
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
    user = request.user
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(id = prod_id)
    Cart(user = user,product=product).save()
    return redirect('/cart')
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user =user )
        amount = 0 
        shiping_amount = 70 
        
        total_amount = 0
        product_cart = [p for p in Cart.objects.all() if p.user == user]
        if product_cart:
            prod_quantity = 0
            for p in product_cart:
                amount = (p.quantity *p.product.discounted_price)
                total_amount += amount
                prod_quantity+=1
            shiping_amount *=prod_quantity
            if total_amount >=1000:
                shiping_amount =0
                total = (total_amount+shiping_amount)+ (total_amount+shiping_amount)*18/100
            else:
                total = total_amount+shiping_amount

                
        return render(request, 'app/addtocart.html',{'carts' :cart,'total':total,'total_amount':total_amount,'shiping_amount':shiping_amount})
def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html',{'active': 'btn-primary'})

def address(request):
    add = Customer.objects.filter(user= request.user)
    return render(request, 'app/address.html',{'add' : add,'active ':'btn-primary'})

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
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user = user,name= name,locality = locality,city = city,zipcode = zipcode,state=state,)
            reg.save()
            messages.success(request ,'Congratulations!! Acount Updated.')
        return render(request, 'app/profile.html',{'form':form})