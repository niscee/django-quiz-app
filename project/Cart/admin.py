from django.contrib import admin
from .models import UserCartStatus, CartProduct

# Register your models here.
admin.site.register(UserCartStatus)
admin.site.register(CartProduct)