from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import HttpResponse


from .serializers import UserSerializer, SurveySerializer, QuestionSerializer
from .models import Survey, Question

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Surveys to be viewed or edited.
    """
    queryset = Survey.objects.all()#.order_by('-id')
    serializer_class = SurveySerializer
    
class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be viewed or edited.
    """
    queryset = Question.objects.all()#.order_by('-id')
    serializer_class = QuestionSerializer
    
# def index(request):
#     return HttpResponse("Hello World!")