from django.shortcuts import render, redirect
from django.contrib import messages
from coffeshop.products.models import Category, Product
# Create your views here.

def index(request):
     products = Product.objects.all()
     # products = Product.objects.filter(trending=1)   
     return render(request, "common/index.html", {"products": products})



def catalogue(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}

    return render(request, 'products/catalogue.html', context)


def catalogue_view(request, name):
    category = Category.objects.filter(name=name, status=0)
    products = Product.objects.filter(category__name=name)
    context = {
        'category__name': name,
        'products': products,
    }

    if category:
        return render(request, 'common/index.html', context)
    else:
        messages.warning(request, 'No such Category found')
        return redirect('catalogue.html')


def product_details(request, cat_name, pro_name):
    category = Category.objects.filter(name=cat_name, status=0)
    products = Product.objects.filter(name=pro_name, status=0)
    if category:
        if products:
            products = Product.objects.filter(name=pro_name, status=0).first()
            return render(request, 'products/product-details.html', {'products': products})
        else:
            messages.error(request, 'No such Product found')
            return redirect('catalogue')

    else:
        messages.error(request, 'No such Category found')
        return redirect('catalogue')