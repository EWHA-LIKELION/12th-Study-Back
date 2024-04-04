from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone

# Create your views here.

def home(request):
    questions = Question.objects
    return render(request, 'home.html', {'questions':questions})

def detail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question':question_detail})

def new(request):
    return render(request, 'new.html')
    
def create(request):
    new_question = Question()
    new_question.content = request.POST['body']
    new_question.title = request.POST['title']
    new_question.update_time = timezone.now()
    new_question.save()
    return redirect('home')

def delete(request, question_id):
    question_delete=get_object_or_404(Question, pk=question_id)
    question_delete.delete()
    return redirect('home')

def update_page(request, question_id):
    question_update = get_object_or_404(Question, pk=question_id)
    return render(request, 'update.html', {'question':question_update})

def update(request, question_id):
    question_update = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        title = request.POST.get('title', '')  
        content = request.POST.get('body', '')  
        question_update.title = title
        question_update.content = content
        question_update.save()
        return redirect('home')
    else:
        return render(request, 'update.html', {'question': question_update})