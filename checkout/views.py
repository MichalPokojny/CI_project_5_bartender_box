from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N9vCOKIWhJzoHAXk1JfSI1sBZL39Av0peAXL7dAZ7IoNJuOLNy60TmTaQuzXHmFZrdTIlSs3Nf8JIU2zHsJ7VTE00CYatc33y'
    }

    return render(request, template, context)
