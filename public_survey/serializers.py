from rest_framework import serializers
from .models import Survey, Question
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # ['url', 'username', 'email']

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__' # ['title', 'start_date', 'end_date', 'description', 'author']
        
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__' # ['survey', 'text', 'type_question']