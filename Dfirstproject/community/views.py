from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Question

# Create your views here.

def List(request):
    questions= Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':questions})

#def home(request):
#    questions=Question.objects
#    return render(request, 'home.html', {'post':questions})

def detail(request, question_id):
    question_detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'post': question_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post=Question()
    new_post.title=request.POST['title']
    new_post.content=request.POST['body']
    new_post.date=timezone.now()
    new_post.save()
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
