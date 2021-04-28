from django.shortcuts import render, redirect
from .forms import QuizForm
from django.contrib import messages
from .models import Question
from django.contrib.auth.decorators import login_required


URL = 'Authentication:login'

# instructor controller
@login_required(login_url=URL)
def home(request):
    questions = Question.objects.order_by('id')
    context = {'questions': questions}
    return render(request, 'dashboard/quizlist.html', context)

@login_required(login_url=URL)
def addQuestion(request):
    if request.method == "POST":
        QUIZ_FORM = QuizForm(request.POST)
        if QUIZ_FORM.is_valid():
            QUIZ_FORM.save()
            messages.success(request, 'Added Successfully.')

    QUIZ_FORM = QuizForm()
    context = {'QUIZ_FORM': QUIZ_FORM}
    return render(request, 'dashboard/addquestion.html', context)  


@login_required(login_url=URL)
def deleteQuestion(request, id):
    q = Question.objects.get(id=id) 
    if q:
        q.delete() 
        messages.success(request, 'Course Deleted Successfully!!')
        return redirect('Question:quiz') 
    
    context = {}
    messages.success(request, 'something went wrong!!')
    return render(request, 'dashboard/quiz.html', context) @login_required(login_url=URL)


def editQuestion(request, id):
    q = Question.objects.get(id=id)
    if request.method == "POST":
        form = QuizForm(request.POST, instance=q)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question Details Updated Successfully!!')

    form = QuizForm(instance=q)       
    context = {'form': form}
    return render(request, 'dashboard/quiz_update.html', context)    



# student controller.
def startQuiz(request):
    context = {}
    return render(request, 'dashboard/startquiz.html', context)



def QuizProgress(request):
    attempt, created = QuizAttempt.objects.get_or_create(
            user_id = request.user.id,
            status = False
        )
    context = {}
    return render(request, 'dashboard/startquiz.html', context)