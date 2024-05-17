from django.shortcuts import render, get_object_or_404, redirect , HttpResponse
from .models import *
from django.utils import timezone
from .forms import *

# Create your views here.

def home(request):
    questions=Question.objects
    return render(request, 'home.html', {'questions': questions})

def detail(request,question_id):
    question_detail = get_object_or_404(Question, pk= question_id)
    question_hashtag=question_detail.hashtag.all()
    
    return render(request, 'detail.html', {'question': question_detail, 'hashtags':question_hashtag})

def new(request):
    form=QuestionForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    form=QuestionForm(request.POST, request.FILES)
    if form.is_valid():
        new_post=form.save(commit=False)
        new_post.date=timezone.now()
        new_post.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_post.hashtag.add(new_hashtag[0])
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

def add_comment(request, question_id):
    blog = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail', question_id)
    
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form })


