from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Product
from .models import CartItem


def index(request):
    """View function for home page of site."""
    num_product = Product.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_product': num_product,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        cart_item = CartItem(product=product, user=request.user)
        cart_item.save()
        return redirect('cart')


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('my_cart')


@login_required
def my_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items()
    total_price = cart.total_price
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'catalog/my_cart.html', context)


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        # Handle payment processing and order creation
        # ...
        # After successful payment and order creation, clear cart
        cart.items.clear()
        return redirect('order_success')
    return render(request, 'catalog/checkout.html', {'cart': cart})


def order_success(request):
    return render(request, 'catalog/order_success.html')