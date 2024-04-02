from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import Question

# Create your views here.

def List(request):
    posts = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'post':post})