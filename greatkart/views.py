
from dataclasses import is_dataclass
from unicodedata import category
from django.shortcuts import render
from store.models import Product
from category.models import Category

def home(request):
    products = Product.objects.all().filter(is_available=True, category=1)
    personal_care=Product.objects.all().filter(is_available=True, category=2)
    herbal=Product.objects.all().filter(is_available=True, category=3)
    categories=Category.objects.all()
   
    

    context = {
        'products': products,
        'personal':personal_care,
        'categories':categories,
        'herbal':herbal
        
    }
    return render(request, 'home.html', context)
