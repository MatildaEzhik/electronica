from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import CheckoutForm
from shop.models import Product, Order


def home(request):
    products = Product.objects.filter(status='POPULAR')[:5]
    new_products = Product.objects.filter(status='NEW')[:5]
    discounted_products = Product.objects.filter(status='DISCOUNT')[:5]
    return render(request, 'shop/home.html', {
        'products': products,
        'new_products': new_products,
        'discounted_products': discounted_products,
    })

def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'reviews': reviews
    })

def cart(request):
    return render(request, 'shop/cart.html')

@login_required
def checkout(request):
    return render(request, 'shop/checkout.html')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order_history.html', {'orders': orders})



@login_required
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = 'PENDING'
            order.save()
            return redirect('order_history')
    else:
        form = CheckoutForm()
    return render(request, 'shop/checkout.html', {'form': form})
