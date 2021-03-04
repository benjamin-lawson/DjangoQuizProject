from django.urls import include, path
from .views import QuizListViewSet, QuizDetailViewSet, QuizCreateViewSet


urlpatterns = [
    path('', QuizListViewSet.as_view()),
    path('<uuid:pk>/', QuizDetailViewSet.as_view()),
    path('create/', QuizCreateViewSet.as_view()),
    path('<uuid:pk>/questions/', include('Question.urls'))
]