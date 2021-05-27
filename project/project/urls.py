"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('Frontend.urls', 'Frontend'), namespace='Frontend')),

    # cart operations.
    path('cart-add/', include(('Cart.urls', 'Cart'), namespace='Cart')),

    # login/logout.
    path('authentication/', include(('Authentication.urls',
         'Authentication'), namespace='Authentication')),

    # backend operations.     
    path('dashboard/', include(('Dashboard.urls', 'Dashboard'), namespace='Dashboard')),
    path('course/', include(('CourseCategory.urls', 'CourseCategory'), namespace='CourseCategory')),
    path('quiz/', include(('Quiz.urls', 'Quiz'), namespace='Quiz')),
]
