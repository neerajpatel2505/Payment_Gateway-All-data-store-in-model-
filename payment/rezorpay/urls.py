from django.urls import path
from .import views

urlpatterns = [
    path("",views.item_payment,name='item_payment'),
    path("payment-Status/",views.payment_status,name='payment-status')
]