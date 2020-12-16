from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Survey(models.Model):
    """Атрибуты опроса:название, дата старта, дата окончания, описание."""
    title = models.CharField(max_length=120)
    start_date = models.DateField(editable=True)
    end_date = models.DateField(editable=True, blank=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='survey', on_delete=models.CASCADE)
    
    def __str__(self, ):
        return self.title
    

class Question(models.Model):
    """Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)"""
    QUESTION_CHOICES = [
        ('text', 'Ответ текстом'),
        ('radio', 'Ответ с выбором одного варианта'),
        ('check', 'Ответ с выбором нескольких вариантов'),
    ]    
    survey = models.ForeignKey(Survey, related_name='question', on_delete=models.CASCADE)
    text = models.TextField()
    type_question = models.CharField(max_length=64, choices=QUESTION_CHOICES)

    
class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, verbose_name = "Ответ")
