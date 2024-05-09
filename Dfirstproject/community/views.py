from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Question
from .forms import CommentForm
from .models import *

# Create your views here.

def List(request):
    questions= Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':questions})

#def home(request):
#    questions=Question.objects
#    return render(request, 'home.html', {'post':questions})

def detail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    question_hashtag=question_detail.hashtag.all()
    question_likes=question_detail.like_users.all()
    return render(request, 'detail.html', {'post': question_detail, 'hashtags':question_hashtag, 'likes':question_likes})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post=Question()
    new_post.title=request.POST['title']
    new_post.content=request.POST['body']
    new_post.date=timezone.now()
    new_post.save()
    hashtags=request.POST['hashtags']
    hashtag=hashtags.split(", ")
    for tag in hashtag:
        new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
        new_post.hashtag.add(new_hashtag[0])
    return redirect('detail', new_post.id)
    return redirect('list')

def delete(request, question_id):
    post_delete=get_object_or_404(Question, pk=question_id)
    post_delete.delete()
    return redirect('list')

def update_page(request,question_id):
    blog_update=get_object_or_404(Question, pk=question_id)
    return render(request,'update.html', {'question':blog_update})

def update(request, question_id):
    blog_update = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        title = request.POST.get('title', '')  
        body = request.POST.get('body', '')  
        blog_update.title = title
        blog_update.content = body
        blog_update.save()
        return redirect('list')
    else:
        return render(request, 'update.html', {'question': blog_update})

def add_comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment= form.save(commit=False)
            comment.post= question
            comment.save()
            return redirect('detail', question_id)

    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form})

def likes(request, question_id):
    article = get_object_or_404(Question, pk=question_id)

    if request.user.is_authenticated:
        user_id = request.user.id
        if user_id in article.like_users.all().values_list('id', flat=True):
            article.like_users.remove(user_id)
        else:
            article.like_users.add(user_id)

    return redirect('', question_id=question_id)

