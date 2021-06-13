from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.core.paginator import EmptyPage, Paginator

# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searchbar', False)
        searched_products = Product.objects.filter(title__icontains=searched)

        return render (request, 'search.html', {'searched': searched, 'products':searched_products})

def category_list (request,category_slug=None):
    category_name = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category_name)
    p = Paginator(products, 20)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'category.html', {'category_name': category_name, 'products':page})

class indexView(ListView):
    model = Product
    template_name = './main.html'


class ItemDetailView(DetailView):
    model = Product
    template_name = './products_detail.html'




def payment(request):
    return render(request,'payment.html')



def delivery(request):
    return render(request,'delivery.html')


def contacts(request):
    return render(request,'contacts.html')

def policy(request):
    return render(request,'policy.html')

