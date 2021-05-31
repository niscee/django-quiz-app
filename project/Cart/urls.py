from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.cartAdd, name='cartAdd'),
    path('checkout/', views.checkout, name='checkout'),
    path('<str:id>/delete/', views.cartDelete, name='cartDelete'),
    path('<str:id>/update/', views.cartDelete, name='cartUpdate'),
    path('payment/', views.payment, name='payment'),
    path('clear-cart/', views.cartClear, name='clearCart'),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
