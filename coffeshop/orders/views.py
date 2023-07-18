from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from coffeshop.orders.models import Favourite, Cart
from coffeshop.products.models import Product


# Create your views here.
def favourite_view_page(request):
    if request.user.is_authenticated:
        favourite = Favourite.objects.filter(user=request.user)
        context = {'favourite': favourite}
        return render(request, 'orders/favourite.html', context)
    else:
        redirect('/')


def remove_favourite(request, fav_id):
    item = Favourite.objects.filter(id=fav_id).get()
    item.delete()
    return redirect('favourite view page')



def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        context = {'cart': cart}
        return render(request, 'orders/cart.html', context)
    else:
        return redirect('/')




def remove_cart(request, cart_id):
    cart_item = Cart.objects.filter(id=cart_id).get()
    cart_item.delete()
    return redirect('cart')


def favourite_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['pid']
            product_status = Product.objects.filter(id=product_id).get()
            favourite = Favourite.objects.filter(user=request.user.id, product_id=product_id)
            if product_status:
                if favourite:
                    return JsonResponse({'status': 'Product already in Favourite'}, status=200)
                else:
                    Favourite.objects.create(user=request.user, product_id=product_id)
                    return JsonResponse({'status': 'Product successfully added to Favourite'}, status=200)
        return JsonResponse({'status': 'Login to add Favourite'}, status=200)
    return JsonResponse({'status': 'Invalid access!'}, status=200)


def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            product_status = Product.objects.filter(id=product_id).get()
            cart = Cart.objects.filter(user=request.user.id, product_id=product_id)
            if product_status:
                if cart:
                    return JsonResponse({'status': 'Product already in Cart'}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'Product successfully added to Cart'})
                    else:
                        return JsonResponse({'status': 'Product currently unavailable'}, status=200)
        return JsonResponse({'status': 'Login to add Cart'}, status=200)
    return JsonResponse({'status': 'Invalid access!'}, status=200)