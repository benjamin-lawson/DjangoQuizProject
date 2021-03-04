from django.db import models
from Quiz.models import Quiz
import uuid


class Question(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=128)
    order = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quiz.user.username} | {self.quiz.title} | {self.text}'

    class Meta:
        ordering = ['quiz', 'order']
