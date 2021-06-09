from django.urls import path
from .views import create_order

app_name = 'orders'

urlpatterns = [
    path('order_creation/',create_order, name='create_order'),
]