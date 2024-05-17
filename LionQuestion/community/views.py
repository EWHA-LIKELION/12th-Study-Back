from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, HashTag
from .forms import QuestionForm, CommentForm
from django.utils import timezone


# Create your views here.
def home(request):
    questions = Question.objects
    return render(request, 'home.html', {'questions':questions})

def detail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    question_hashtag = question_detail.hashtag.all()
    return render(request, 'detail.html', {'question':question_detail, 'hashtags':question_hashtag})

def new(request):
    return render(request, 'new.html')
    
def create(request):
    form = QuestionForm(request.Post, request.FILES)
    if form.is_vaild() :
        new_question = Question()
        new_question.content = request.POST['body']
        new_question.title = request.POST['title']
        new_question.update_time = timezone.now()
        new_question.save()

        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_question.hashtag.add(new_hashtag[0])
        return redirect(request, 'detail.html', new_question.id)
    return redirect('home')

def likes(request, question_id):
    if request.user.is_authenticated:
        question = get_object_or_404(Question, pk=question_id)

        if question.likes.filter(pk=request.user.pk).exists():
            question.likes.remove(request.user)
        else:
            question.likes.add(request.user)
        return redirect('detail', question_id=question_id)
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
    
def add_comment(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.save()
            return render(request, 'detail.html', {'question': question})
    else : 
        form = CommentForm()
    return render(request, 'add_comment.html', {'form':form})