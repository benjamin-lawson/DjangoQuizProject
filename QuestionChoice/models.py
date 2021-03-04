from django.db import models
import uuid
from Question.models import Question


class QuestionChoice(models.Model):
    choice_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    value = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.question.quiz.user.username} | {self.question.quiz.title} | {self.question.text} | {self.value}'

    class Meta:
        ordering = ['-create_date']
