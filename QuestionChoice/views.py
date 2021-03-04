from rest_framework import generics, permissions
from .models import QuestionChoice
from .serializers import QuestionChoiceSerializer


class QuestionChoiceListViewSet(generics.ListCreateAPIView):
    queryset = QuestionChoice.objects.all()
    serializer_class = QuestionChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return QuestionChoice.objects.filter(question__question_id__exact=self.kwargs['pk'])
        return QuestionChoice.objects.filter(question__quiz__user=self.request.user)


class QuestionChoiceDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionChoice.objects.all()
    serializer_class = QuestionChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]