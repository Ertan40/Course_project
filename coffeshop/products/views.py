from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from coffeshop.products.forms import ProductCreateForm, ProductEditForm
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


@login_required
def add_product(request):
    if request.POST == 'GET':
        form = ProductCreateForm()
    else:
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product list')

    context = {'form': form}
    return render(request, 'products/add-product.html', context)


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = ProductEditForm(instance=product)
    else:
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product list')

    context = {'form': form, 'product': product}

    return render(request, 'products/edit-product.html', context)


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product list')

    return render(request, 'products/delete-product.html', {'product': product})


@login_required
def product_list(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'products/product-list.html', context)


