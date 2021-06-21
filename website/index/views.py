from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .forms import Comment_form
from .models import Product, Category, Comment
from django.core.paginator import EmptyPage, Paginator

# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def products(request):
    return {
        'featured_products': Product.objects.all()
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

    def get(self,request,pk):
        commentForm = Comment_form()
        object = Product.objects.filter(id=pk)
        product = Product.objects.get(id=pk)
        id = product.id
        comments = Comment.objects.filter(product_id=id)
        return render(request, self.template_name, {'object':object, 'form':commentForm, 'comments': comments})
    
    def post(self,request,pk):
        if request.user.is_authenticated:
            commentForm = Comment_form(request.POST)
            user = request.user
            object = Product.objects.get(id=pk)
            id = object.id
            if commentForm.is_valid():
                Comment.objects.create(product_id=id,user=user,body=commentForm.cleaned_data['body'])
                return render(request,'comment_saved.html')
        else:
            return redirect('account:login')




def payment(request):
    return render(request,'payment.html')



def delivery(request):
    return render(request,'delivery.html')


def contacts(request):
    return render(request,'contacts.html')

def policy(request):
    return render(request,'policy.html')

