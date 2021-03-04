from django.db import models
from django.contrib.auth.models import User
import uuid


class Quiz(models.Model):
    quiz_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    primary_color = models.CharField(max_length=7, default='#cccccc')
    secondary_color = models.CharField(max_length=7, default='#999999')
    background_color = models.CharField(max_length=7, default='#444444')

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.title}'

    class Meta:
        verbose_name_plural = 'Quizzes'
        ordering = ['-create_date', 'title']
