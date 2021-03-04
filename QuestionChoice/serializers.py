from rest_framework import serializers
from .models import QuestionChoice


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = ['choice_id', 'value', 'question', 'create_date']