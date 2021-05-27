from django.db import models
from django.conf import settings
from CourseCategory.models import Product

# Create your models here.
class UserCartStatus(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
    
    @property
    def cartTotalQty(self):
        carts =  self.cartproduct_set.all() 
        count = sum([cart.quantity for cart in carts])
        return count



class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    UserCartStatus = models.ForeignKey(UserCartStatus, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        return str(self.user) 

