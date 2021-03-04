from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', obtain_jwt_token),
    path('quiz/', include('Quiz.urls'), name='quiz'),
    path('question/', include('Question.urls'), name='question'),
    path('choice/', include('QuestionChoice.urls'), name='choice'),
    path('schema/', include('Documentation.urls'), name='documentation'),
]
