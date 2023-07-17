from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutPage,name="logout"),
    path('detail/',views.detail,name="detail"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('search/',views.search,name="search"),
    path('category/',views.category,name="category"),
    #paypal
    path('paypal/',include('paypal.standard.ipn.urls')),
    #payment successful 
    path("payment-completed/", views.payment_completed_view, name="payment-completed"),

    path("payment-failed/", views.payment_failed_view, name="payment-failed"),
    #//////////////////
    path('process_order/',views.processOrder,name="process_order"),



    
    

]
