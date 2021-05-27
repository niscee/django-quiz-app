from django.shortcuts import render
from django.http import HttpResponse
from CourseCategory.models import Product
from Slider.models import Slider
from CourseCategory.models import CourseCategory
from Cart.models import UserCartStatus, CartProduct

def index(request):
    products = Product.objects.order_by('id')[:4]
    sliders = Slider.objects.order_by('id')

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    context = {'products': products, 'sliders': sliders, 'userCartStatus': userCartStatus}
    return render(request, 'frontend/layout/index.html', context)


def products(request):
    products = Product.objects.order_by('id')
    categories = CourseCategory.objects.order_by('id')

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    context = {'products': products, 'categories': categories, 'userCartStatus': userCartStatus}
    return render(request, 'frontend/all_product.html', context)


def singleProduct(request, id):
    product = Product.objects.get(id=id)
    
    # check if product of certain category is available or not, if not send none.
    if products:
        title = Product.objects.filter(CourseCategory_id=id)
    else:
        title = "None"  

    
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}
          
    
    categories = CourseCategory.objects.order_by('id')
    context = {'product': product, 'categories': categories, 'title': title, 'userCartStatus': userCartStatus}
    return render(request, 'frontend/singleproduct.html', context)    
