from django.shortcuts import render
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
