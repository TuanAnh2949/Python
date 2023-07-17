import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#paypal
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.
#detail
    
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartItems= order.get_cart_items
        user_not_login ="hidden"
        user_login="show"
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems= order['get_cart_items']
        user_not_login ="show"
        user_login="hidden"
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub = True)
    context = {'products':products,'items': items, 'order': order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/detail.html', context)
def category(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartItems= order.get_cart_items
        user_not_login ="hidden"
        user_login="show"
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0}
        cartItems= order['get_cart_items']
        user_not_login ="show"
        user_login="hidden"
    categories = Category.objects.filter(is_sub = True)
    active_category = request.GET.get('category','')
    if active_category :
        products = Product.objects.filter(category__slug= active_category)
    context = {'categories': categories,'products':products,'active_category':active_category,'items': items, 'order': order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/category.html', context)

def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartItems= order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems= order['get_cart_items']
   
    categories = Category.objects.filter(is_sub = True)
    products = Product.objects.all()
    return render(request,'app\search.html',{"searched":searched,"keys":keys,'products': products,'cartItems':cartItems,'categories': categories})
def register(request):
    form = CreateUserForm()
  
    if request.method == "POST":
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={'form':form}
    return render(request, 'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request, 'tài khoản hoặc mật khẩu của bạn không đúng!')

    context ={}
    return render(request, 'app/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartItems= order.get_cart_items
        user_not_login ="hidden"
        user_login="show"
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
        cartItems= order['get_cart_items']
        user_not_login ="show"
        user_login="hidden"
    categories = Category.objects.filter(is_sub = True)
    products = Product.objects.all()
    context = {'categories': categories,'products': products,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/home.html', context)


    
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartItems= order.get_cart_items
        user_not_login ="hidden"
        user_login="show"
    else:
        items = []
        order = {'get_cart_items': 0,'get_cart_total': 0, 'shipping':False}
        cartItems= order['get_cart_items']
        user_not_login ="show"
        user_login="hidden"

    #products = Product.objects.all()
    context = {'items': items, 'order': order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/cart.html', context)


def checkout(request):
    # paypal
    # host=request.get_host()
    # paypal_dict ={
    #     'busniess':settings.PAYPAL_RECEIVER_EMAIL,
    #     'amount':'3200',
    #     'item_name': "Order_item-No-4",
    #     'invoice': "INVOICE_NO-3",
    #     'currenry_code':"VND",
       
    #     'notify_url':'http://{}{}'.format(host, reverse("app:paypal-ipn")),
    #     'return_url':'http://{}{}'.format(host, reverse("app:paypal-completed")),
    #     'cancel_url':'http://{}{}'.format(host, reverse("app:paypal-failed")),
        
    # }
    


    # paypal_payment_button = PayPalPaymentsForm(inital= paypal_dict)




    # -------------
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            Customer=customer, complete=False)
        items = order.order_item_set.all()
        cartItems= order.get_cart_items
        user_not_login ="hidden"
        user_login="show"

    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0, 'shipping':False}
        cartItems= order['get_cart_items']
        user_not_login = "show"
        user_login="hidden"
    
   # products = Product.objects.all()
    context = {'items': items, 'order': order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request, 'app/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(Customer=customer, complete=False)
    order_item, created = Order_item.objects.get_or_create(order=order, product=product)
    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()
    if order_item.quantity <= 0:
        order_item.delete()
    return JsonResponse('added', safe=False)

#PAYPAL
def payment_completed_view(request):
    return render(request,'app/payment-completed.html')
def payment_failed_view(request):

    return render(request,'app/payment-failed.html')

#test
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(Customer=customer, complete=False)
        total = float (data['form']['total'])
        order.transaction_id = transaction_id

        if total == float( order.get_cart_total):
            order.complete =True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                mobile = data['shipping']['mobile'],
                zipcode = data['shipping']['zipcode'],
            )


    else:
        print('User is not loggin')
    return JsonResponse('Payment complete!',safe=False)