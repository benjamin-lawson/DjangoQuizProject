from rest_framework import serializers
from .models import Quiz
from Question.serializers import DetailedQuestionSerializer


class GenericQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quiz_id', 'title']


class DetailQuizSerializer(serializers.ModelSerializer):
    questions = DetailedQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'
