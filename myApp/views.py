from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, "myApp/home.html")


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "myApp/products.html", context)