from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import Question

# Create your views here.

def List(request):
  questions = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  return render(request, 'list.html', {'posts': questions})

def detail(request, pk):
  question = get_object_or_404(Question, pk=pk)
  return render(request, 'detail.html', {'post': question})

# 여기서 'posts'와 'post'를 'question'으로 바꿔서 rendering이 안되는 일이 발생
