from django.shortcuts import redirect
from django.http import HttpResponse

def access(allowed=[]):
    def wrapper(func):
        def inner(request, *args, **kwargs):
            if request.user.userprofile.user_type in allowed:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('You dont have permission to access this page.')
        return inner 
    return wrapper
       