from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from index.models import Product

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    subtotal = float(basket.get_total_price())
    if float(subtotal)==float(0):
        return render(request, 'index_basket/summary.html', {'basket': basket})
    else:
        return render(request, 'index_basket/summary.html', {'basket': basket, 'subtotal': float(subtotal)})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response
    


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = float(basket.get_total_price())
        response = JsonResponse({'qty': basketqty, 'subtotal': float(baskettotal)})
        return response