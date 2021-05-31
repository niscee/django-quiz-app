from django.shortcuts import render, redirect
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
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

def contact(request):
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    if request.method == "POST":
        # sending email
        template = render_to_string('frontend/msgsample.html', {
                                    'msg': request.POST['msg'], 'email': request.POST['email'], 'phone': request.POST['phone'], 'name': request.POST['name']})
        email = EmailMessage(

            'DIY Eplatform',
            template,
            settings.EMAIL_HOST_USER,
            ['rananischal15@gmail.com'],
        )

        email.fail_silently = False
        email.send()
        
        context = {'userCartStatus': userCartStatus}
        messages.success(request, 'We Will Contact You Soon!!')
        return redirect("Frontend:contact")


    context = {'userCartStatus': userCartStatus}
    return render(request, 'frontend/contact.html', context)



