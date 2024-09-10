from django import forms

from shop.models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['description']
