from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = "Products"),
    path('cart/' , views.cart , name = "cart"), 
    path('checkout', views.checkout , name = "checkout"),
]