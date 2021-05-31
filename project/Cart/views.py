from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.conf import settings
from .models import CartProduct, UserCartStatus
from CourseCategory.models import Product
import json

# Create your views here.


def cartAdd(request):
    data = json.loads(request.body)
    product = Product.objects.get(id=data['product_id'])

    # get active UserCartStatus.
    userCartStatus, created = UserCartStatus.objects.get_or_create(
        user_id=request.user, complete=False)
    
    product = CartProduct(
        product=product, quantity=1, user=request.user, UserCartStatus=userCartStatus)
    product.save()

    return JsonResponse({"msg": "successful"})


# site checkout page.
def checkout(request):
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    context = {'userCartStatus': userCartStatus}
    return render(request, 'frontend/checkout.html', context)


# site cart delete func.
def cartDelete(request, id):
    id = int(id)
    product = CartProduct.objects.get(id=id)
    product.delete()
    return JsonResponse({"msg": "successful"})   



# site cart payment func.
def payment(request):
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}



    context = {'userCartStatus': userCartStatus}
    return render(request, 'frontend/payment.html', context)


# site cart clear func.
def cartClear(request):
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
        userCartStatus.complete = True
        userCartStatus.save()  
        return JsonResponse({"msg": "successful"})  
    else:
        userCartStatus = {}
    
