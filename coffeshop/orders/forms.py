from django import forms
from coffeshop.orders.models import Order


class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)

# class CheckoutForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('address', 'phone')
#
#         widgets = {
#                 'address': forms.TextInput(),
#                 'phone': forms.NumberInput(),
#         }
