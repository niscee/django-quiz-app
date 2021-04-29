from django.shortcuts import render
from UserProfile.forms import UserProfileForm
from Authentication.forms import UpdateRegisterForm
from UserProfile.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



URL = 'Authentication:login'

# admin dashboard home page.
@login_required(login_url=URL)
def dashboard(request):
    user = UserProfile.objects.get(user_id=request.user)
    context = {'user': user}
    return render(request, 'dashboard/main.html', context)


# dashboard user and profile update form. 
@login_required(login_url=URL)
def profile(request):
    user_profile_id = UserProfile.objects.get(user_id=request.user.id)

    if request.method == "POST":
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile_id)
        user_form = UpdateRegisterForm(request.POST, instance=request.user)
        if user_profile_form and user_form.is_valid():
            user_profile_form.save()
            user_form.save()
            messages.success(request, 'Profile Updated Successfully!!')
    
    USERPROFILE_FORM = UserProfileForm(instance=user_profile_id)
    USER_FORM = UpdateRegisterForm(instance=request.user)
    context = {'USERPROFILE_FORM': USERPROFILE_FORM, 'USER_FORM': USER_FORM}
    return render(request, 'dashboard/userprofile/profile.html', context)