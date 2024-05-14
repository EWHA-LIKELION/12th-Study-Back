from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import *
from .forms import *
# Create your views here.

def List(request):
  questions = Question.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
  return render(request, 'list.html', {'questions': questions})

def detail(request, pk):
  question = get_object_or_404(Question, pk=pk)
  question_hashtag = question.hashtag.all()
  return render(request, 'detail.html', {'question': question, 'hashtags':question_hashtag})

# 여기서 'posts'와 'post'를 'question'으로 바꿔서 rendering이 안되는 일이 발생! 왜지?

def new(request):
  form = PostForm()
  return render(request, 'new.html', {'form': form})
  # return render(request, 'new.html')

def create(request):
  form = PostForm(request.POST, request.FILES)
  if form.is_valid():
    new_question=form.save(commit=False)
    new_question.upload_time = timezone.now()
    new_question.save()
    hashtags = request.POST['hashtags']
    hashtag = hashtags.split(", ")
    for tag in hashtag:
      new_hashtag = HashTag.objects.get_or_create(hashtag=tag)
      new_question.hashtag.add(new_hashtag[0])
    return redirect('detail', new_question.id)
  return redirect('main')
  # new_question = Question()
  # new_question.title = request.POST['title']
  # new_question.content = request.POST['content']
  # new_question.upload_time = timezone.now()
  # new_question.save()
  return redirect('main')

def delete(request, pk):
  question_delete=get_object_or_404(Question,pk=pk)
  question_delete.delete()
  return redirect('main')

# def update_page(request, pk):
#   question_update=get_object_or_404(Question, pk=pk)
#   return render(request, 'update.html', {'post': question_update})

# def update(request, pk):
#     question_update = get_object_or_404(Question, pk=pk)
#     if request.method == 'POST':
#         title = request.POST.get('title', '')  
#         content = request.POST.get('content', '')  
#         question_update.title = title
#         question_update.content = content
#         question_update.save()
#         return redirect('main')
#     else:
#         return render(request, 'update.html', {'post': question_update})

def update_page(request, pk):
  question_update=get_object_or_404(Question, pk=pk)
  form = PostForm(instance=question_update)
  return render(request, 'update.html', {'form': form, 'question': question_update})


def update(request, pk):
  question_update=get_object_or_404(Question, pk=pk)
  if request.method=='POST':
    form = PostForm(request.POST, request.FILES, instance=question_update)
    if form.is_valid():
      question_update = form.save(commit=False)
      question_update.save()
      return redirect('detail', pk)
    else:
      return redirect('detail', pk)
  else:
    form = PostForm(instance=question_update)
    return render(request, 'update.html', {'form': form, 'question': question_update})

# def add_comment(request, pk):
#   community = CommentForm(request.POST)

#   if request.method == 'POST':
#     form = CommentForm(request.POST)

#     if form.is_valid():
#       comment = form.save(commit=False)
#       comment.post = community
#       comment.save()
#       return redirect('detail', pk)
    
#   else:
#     form = CommentForm()
  
#   return render(request, 'add_comment.html', {'form': form})

def add_comment(request, pk):
    # pk는 어떤 질문(Question)에 대한 ID인지를 나타냅니다.
  if request.user.is_authenticated:
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.user= request.user
            # if (comment.is_like):
            #   question.like_count = question.like_count + 1
            # question.save()
            comment.save()
            return redirect('detail', pk)

    else:
        form = CommentForm()

        return render(request, 'add_comment.html', {'form': form})

def comments_delete(request, pk, comment_pk):
  if request.user.is_authenticated:
    comment = get_object_or_404(Comment, pk = comment_pk)
    if request.user == comment.user:
      comment.delete()
  return redirect('detail', pk)

# def add_recommend(request, pk):
#   question = get_object_or_404(Question, pk=pk)
#   if request.method == 'POST':
#     form = RecommendForm(request.POST)

#     if form.is_valid():
#       recommend = form.save(commit=False)
#       recommend.question = question
#       if (recommend.is_recommend):
#         question.recommend_count = question.recommend_count + 1
#       question.save()
#       recommend.save()
#       return redirect('detail', pk = pk)
#   else:
#     form = RecommendForm()
#     return render(request, 'add_recommend.html', {'form': form})

def likes(request, pk):
  if request.user.is_authenticated:
    question = get_object_or_404(Question, pk = pk)
    if question.like_users.filter(pk=request.user.pk).exists():
      question.like_users.remove(request.user)
    else:
      question.like_users.add(request.user)

    return redirect('detail', pk)
  return redirect('login')