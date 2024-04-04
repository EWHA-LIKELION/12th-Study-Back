from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
# Create your views here.

def home(request):
    questions=Question.objects
    return render(request, 'home.html', {'questions': questions})

def detail(request,question_id):
    question_detail = get_object_or_404(Question, pk= question_id)
    return render(request, 'detail.html', {'question': question_detail})

def new(request):
    form=QuestionForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    form=QuestionForm(request.POST, request.FILES)
    if form.is_valid():
        new_post=form.save(commit=False)
        new_post.date=timezone.now()
        new_post.save()
        return redirect('detail', new_post.id)
    return redirect('home')

def delete(request, question_id):
    question_delete=get_object_or_404(Question, pk=question_id)
    question_delete.delete()
    return redirect('home')

def new(request):
    form=QuestionForm()
    return render(request, 'new.html',{'form': form})

def update_page(request, question_id):
    question_update= get_object_or_404(Question,pk=question_id)
    return render(request,'update.html', {'question': question_update})

def update(request, question_id):
    question_update=get_object_or_404(Question,pk=question_id)
    question_update.title= request.POST['title']
    question_update.body=request.POST['body']
    question_update.save()
    return redirect('home')
