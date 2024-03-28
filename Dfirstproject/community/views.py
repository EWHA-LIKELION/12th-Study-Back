from django.shortcuts import render, get_object_or_404
from django.utils import  timezone
from community.models import Question
# Create your views here.

def List(request):
    questions = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'questions': questions})

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'question':question})