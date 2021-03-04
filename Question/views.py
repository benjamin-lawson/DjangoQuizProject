from rest_framework import permissions, generics
from .serializers import GenericQuestionSerializer, DetailedQuestionSerializer
from .models import Question


class QuestionListViewSet(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = GenericQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Question.objects.filter(quiz__quiz_id__exact=self.kwargs['pk'])
        return Question.objects.filter(quiz__user=self.request.user)


class QuestionCreateViewSet(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = DetailedQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = DetailedQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
