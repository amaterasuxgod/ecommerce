from django.shortcuts import render
from .forms import OrderForm
from basket.basket import Basket
from .models import Order, OrderItem
from django.http.response import HttpResponse
# Create your views here.

def create_order(request):
    basket = Basket(request)
    if request.method == 'POST':
        user = request.user.id
        basket_total = basket.get_total_price()
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid():
         order = Order.objects.create(user_id=user, full_name=orderForm.cleaned_data['name'], address1=orderForm.cleaned_data['adress1'],
                                phone=orderForm.cleaned_data['phone'], total_price=basket_total, city=orderForm.cleaned_data['city'])

         order_id = order.pk

         for item in basket:
             OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])
         basket.clear()
         return render(request, 'orders/order_confirmation.html')
    else:
        registerForm = OrderForm()
    return render(request, 'orders/order_creation.html', {'form': registerForm})



def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    return orders