from django.urls import path
from .views import indexView, ItemDetailView, category_list, search, payment, delivery, contacts, policy

app_name = 'index'

urlpatterns = [
    path('homepage/', indexView.as_view(), name="products-list"),
    path('categories/<slug:category_slug>', category_list, name="category_list"),
    path('searched/', search, name='search'),
    path('pc/<int:pk>/', ItemDetailView.as_view(), name='pc-detail'),
    path('payment/', payment, name='payment'),
    path('delivery/', delivery, name='delivery'),
    path('contacts/', contacts, name='contacts'),
    path('policy/', policy, name='policy'),
]