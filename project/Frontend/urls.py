from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('<str:id>/product/', views.filterproduct, name='product'),
    path('<int:id>/product-details/', views.singleProduct, name='singleproduct'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
