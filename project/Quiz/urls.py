from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='quiz'),
    path('add-question', views.addQuestion, name='addQuestion'),
    path('<int:id>/delete-question', views.deleteQuestion, name='deleteQuestion'),
    path('<int:id>/edit-question', views.editQuestion, name='editQuestion'),
    path('start-quiz', views.startQuiz, name='startQuiz'),
    path('quiz-progress', views.progressQuiz, name='progressQuiz'),
    path('quiz-submit', views.submitQuiz, name='submitQuiz'),
    path('quiz-leaderboard', views.leaderBoard, name='leaderBoard'),
    path('<int:id>/quiz-feedback', views.feedback, name='feedback'),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
