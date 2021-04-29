from django.shortcuts import render, redirect
from .forms import QuizForm
from django.contrib import messages
from .models import Question, QuizAttempt, QuizPoint
from UserProfile.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


URL = 'Authentication:login'
TUTORURL = 'dashboard/quiz/teacher'
STUDURL = 'dashboard/quiz/student'

# instructor controller
@login_required(login_url=URL)
def home(request):
    questions = Question.objects.order_by('id')
    context = {'questions': questions}
    return render(request, f'{TUTORURL}/quizlist.html', context)


@login_required(login_url=URL)
def addQuestion(request):
    if request.method == "POST":
        QUIZ_FORM = QuizForm(request.POST)
        if QUIZ_FORM.is_valid():
            QUIZ_FORM.save()
            messages.success(request, 'Added Successfully.')

    QUIZ_FORM = QuizForm()
    context = {'QUIZ_FORM': QUIZ_FORM}
    return render(request, f'{TUTORURL}/addquestion.html', context)


@login_required(login_url=URL)
def deleteQuestion(request, id):
    q = Question.objects.get(id=id)
    if q:
        q.delete()
        messages.success(request, 'Course Deleted Successfully!!')
        return redirect('Quiz:quiz')

    context = {}
    messages.success(request, 'something went wrong!!')
    return render(request, f'{TUTORURL}/quizlist.html', context)


@login_required(login_url=URL)
def editQuestion(request, id):
    q = Question.objects.get(id=id)
    if request.method == "POST":
        form = QuizForm(request.POST, instance=q)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Question Details Updated Successfully!!')

    form = QuizForm(instance=q)
    context = {'form': form}
    return render(request, f'{TUTORURL}/quiz_update.html', context)




# student controller.
@login_required(login_url=URL)
def startQuiz(request):
    context = {}
    return render(request, f'{STUDURL}/startquiz.html', context)


# @login_required(login_url=URL)
# def progressQuiz(request):
#     attempt, created = QuizAttempt.objects.get_or_create(
#             user_id = request.user,
#             status = False
#         )
#     q = Question.objects.order_by('id')
#     count = len(q)

#     # number of data in page.
#     paginator = Paginator(q, 1)
#     page = request.GET.get('page')

#     try:
#         qlist = paginator.page(page)
#     except PageNotAnInteger:
#             # If page is not an integer deliver the first page
#         qlist = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         qlist = paginator.page(paginator.num_pages)


#     context = {'qlist': qlist, 'count': count}
#     return render(request, f'{STUDURL}/progressquiz.html', context)


@login_required(login_url=URL)
def progressQuiz(request):
    attempt, created = QuizAttempt.objects.get_or_create(
        user_id=request.user,
        status=False
    )
    qlist = Question.objects.order_by('?')
    count = len(qlist)

    context = {'qlist': qlist, 'count': count, 'attempt': attempt}
    return render(request, f'{STUDURL}/progressquiz.html', context)


@login_required(login_url=URL)
def submitQuiz(request):

    # getting every data submitted from form.
    anscol = request.POST

    # getting quizAttempt id.
    attempt_id = int(request.POST.get('quizattempt_id'))

    # getting QuizAttempt instance.
    attempt = QuizAttempt.objects.get(id=attempt_id)
    
    # calling countScore function, returns score.
    count = QuizPoint.countScore(anscol)

    # calling countPercentage function, returns percentage.
    quesLen = len(anscol)-2
    percent = QuizPoint.getPercentage(count, quesLen)

    # saving user score in database.
    qscore = QuizPoint(quizattempt_id=attempt, score=count, percentage=percent)
    qscore.save()    
    
    # updating user quiz status.
    attempt.status = True
    attempt.save()
    
    context = {'qscore': qscore, 'quesLen': quesLen}
    return render(request, f'{STUDURL}/quizresult.html', context)

    
def leaderBoard(request):
    profiles = QuizPoint.objects.order_by('-percentage')
    context = {'profiles': profiles}
    return render(request, 'dashboard/quiz/leaderboard.html', context) 
    
