from django.contrib import admin
from .models import CourseCategory, Product, CourseDetail

# Register your models here.
admin.site.register(CourseCategory)
admin.site.register(Product)
admin.site.register(CourseDetail)