from rest_framework import serializers
from .models import Question
from QuestionChoice.serializers import QuestionChoiceSerializer


class GenericQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'text', 'order', 'quiz']


class DetailedQuestionSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['question_id', 'text', 'order', 'choices', 'create_date', 'quiz', 'create_date']