from rest_framework import permissions, generics
from .serializers import GenericQuizSerializer, DetailQuizSerializer
from .models import Quiz


class QuizListViewSet(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = GenericQuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)


class QuizCreateViewSet(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = DetailQuizSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuizDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = DetailQuizSerializer
    permission_classes = [permissions.IsAuthenticated]