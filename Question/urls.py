from django.urls import path, include
from .views import QuestionListViewSet, QuestionCreateViewSet, QuestionDetailViewSet

urlpatterns = [
    path('', QuestionListViewSet.as_view()),
    path('create/', QuestionCreateViewSet.as_view()),
    path('<uuid:pk>/', QuestionDetailViewSet.as_view()),
    path('<uuid:pk>/choices/', include('QuestionChoice.urls'))
]