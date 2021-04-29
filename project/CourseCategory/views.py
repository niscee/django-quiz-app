from django.shortcuts import render, redirect
from .forms import CourseDetailForm
from django.contrib import messages
from .models import CourseDetail
from django.contrib.auth.decorators import login_required
from .decorators import access

# Create your views here.
URL = 'Authentication:login'
TUTORURL = 'dashboard/course/teacher'
STUDURL = 'dashboard/course/student'


@login_required(login_url=URL)
@access(allowed=['TEC'])
def courseAssign(request):
    USER = request.user

    if request.method == "POST":
        form = CourseDetailForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user
            f.save()
            messages.success(request, 'Course Added Successfully!!')

    form = CourseDetailForm()
    courseList = CourseDetail.objects.order_by('-id').filter(user_id=USER)       
    context = {'form': form, 'courseList': courseList}
    return render(request, f'{TUTORURL}/coursedetails.html', context)


@login_required(login_url=URL)
@access(allowed=['TEC'])
def courseDelete(request, id):
    course = CourseDetail.objects.get(id=id) 
    if course:
        course.delete() 
        messages.success(request, 'Course Deleted Successfully!!')
        return redirect('CourseCategory:course') 
    
    context = {}
    messages.success(request, 'something went wrong!!')
    return render(request, f'{TUTORURL}/coursedetails.html', context) 


@login_required(login_url=URL)
@access(allowed=['TEC'])
def courseEdit(request, id):
    course = CourseDetail.objects.get(id=id)
    if request.method == "POST":
        form = CourseDetailForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user
            f.save()
            messages.success(request, 'Course Details Updated Successfully!!')

    form = CourseDetailForm(instance=course)       
    context = {'form': form}
    return render(request, f'{TUTORURL}/coursedetails_update.html', context) 



# usertype(student) controller
@login_required(login_url=URL)
@access(allowed=['STD'])
def courseList(request):
    courseList = CourseDetail.objects.order_by('-id')
    context = {'courseList': courseList}
    return render(request, f'{STUDURL}/courselist.html', context) 


@login_required(login_url=URL)
@access(allowed=['STD'])
def courseSingle(request, id):
    course = CourseDetail.objects.get(id=id)
    context = {'course': course}
    return render(request, f'{STUDURL}/coursesingle.html', context)     