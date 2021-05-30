from django.shortcuts import render
from django.http import HttpResponse
from CourseCategory.models import Product
from Slider.models import Slider
from CourseCategory.models import CourseCategory
from Cart.models import UserCartStatus, CartProduct



# site landing page.
def index(request):
    products = Product.objects.order_by('id')[:4]
    sliders = Slider.objects.order_by('id')

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    context = {'products': products, 'sliders': sliders,
               'userCartStatus': userCartStatus}
    return render(request, 'frontend/layout/index.html', context)


# site all product list page.
def products(request):
    products = Product.objects.order_by('name')
    categories = CourseCategory.objects.order_by('id')

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    context = {'products': products, 'categories': categories,
               'userCartStatus': userCartStatus}
    return render(request, 'frontend/all_product.html', context)


# site filter product list page based on category.
def filterproduct(request, id):

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    if id == "new":
        products = Product.objects.order_by('id')
    elif id == "old":
        products = Product.objects.order_by('-id')
    else:
        products = Product.objects.filter(CourseCategory_id=id)
   
    categories = CourseCategory.objects.order_by('id')

    context = {'products': products, 'categories': categories,
               'userCartStatus': userCartStatus}
    return render(request, 'frontend/all_product.html', context)


# site single product page.
def singleProduct(request, id):
    product = Product.objects.get(id=id)

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    categories = CourseCategory.objects.order_by('id')
    context = {'product': product, 'categories': categories,
               'userCartStatus': userCartStatus}
    return render(request, 'frontend/singleproduct.html', context)


# site contact page.
def contact(request):
    

    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    context = {'userCartStatus': userCartStatus}
    return render(request, 'frontend/contact.html', context)    
