from django.urls import path
from .views import QuestionChoiceListViewSet, QuestionChoiceDetailViewSet

urlpatterns = [
    path('', QuestionChoiceListViewSet.as_view()),
    path('<uuid:pk>/', QuestionChoiceDetailViewSet.as_view())
]