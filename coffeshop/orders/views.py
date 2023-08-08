from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from coffeshop.orders.forms import CheckoutForm
from coffeshop.orders.models import Favourite, Cart, Order
from coffeshop.products.models import Product


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


def checkout_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CheckoutForm(request.POST)
            if form.is_valid():
                address = form.cleaned_data['address']
                phone = form.cleaned_data['phone']
                user = request.user
                cart_items = Cart.objects.filter(user=user)
                # print(cart_items)
                # print(phone)
                # checked and works, so getting the data in order to save in DB
                for cart_item in cart_items:
                    product = cart_item.product
                    price = cart_item.product.price
                    order = Order.objects.create(
                        user=user,
                        product=product,
                        price=price,
                        quantity=cart_item.product_qty,
                        address=address,
                        phone=phone,
                    )
                    order.save()
                # Clear the cart from the session
                request.session['cart'] = {}

                return redirect('order success')  # Redirect to the order success page
        else:
            form = CheckoutForm()

        return render(request, 'orders/checkout.html', {'form': form})
    else:
        return redirect('/')


def order_success_page(request):
    return render(request, 'orders/order-success.html')


def orders_list(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            order = Order.objects.filter(user=request.user)
            # clear the orders from DB
            order.delete()
            return redirect('orders list')
        else:
            # retrieve the orders for the current user
            orders = Order.objects.filter(user=request.user)
            context = {'orders': orders}
            return render(request, 'orders/orders-list.html', context)
    else:
        return redirect('/')


def clear_orders(request):
    if request.user.is_authenticated:
        # Clear the orders from the database
        Order.objects.filter(user=request.user).delete()
    return redirect('orders list')
