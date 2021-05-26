from django.shortcuts import render
from django.http import HttpResponse
from CourseCategory.models import Product
from Slider.models import Slider
from CourseCategory.models import CourseCategory

def index(request):
    products = Product.objects.order_by('id')[:4]
    sliders = Slider.objects.order_by('id')
    context = {'products': products, 'sliders': sliders}
    return render(request, 'frontend/layout/index.html', context)


def products(request):
    products = Product.objects.order_by('id')
    categories = CourseCategory.objects.order_by('id')
    context = {'products': products, 'categories': categories}
    return render(request, 'frontend/all_product.html', context)


def singleProduct(request, id):
    products = Product.objects.filter(CourseCategory_id=id)
    
    if products:
        title = Product.objects.filter(CourseCategory_id=id)[0]
    else:
        title = "None"    
    
    categories = CourseCategory.objects.order_by('id')
    context = {'products': products, 'categories': categories, 'title': title}
    return render(request, 'frontend/all_product.html', context)    
