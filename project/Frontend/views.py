from django.shortcuts import render
from django.http import HttpResponse
from CourseCategory.models import Product

def index(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, 'layout/index.html', context)
