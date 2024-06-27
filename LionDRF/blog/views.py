from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *

# Create your views here.
class QuestionList(views.APIView):
  def get(self, request, format = None):
    
    category = request.GET.get('category')
    order = request.GET.get('order')
    mine = request.GET.get('mine')
    if category:
      questions = Question.objects.filter(category__icontains=category)
    else:
      questions = Question.objects.all()
    if order == "desc":
      questions=questions.order_by('-upload_time')
    if mine and mine.lower() == "true":
      if request.user.is_authenticated:
        questions = questions.filter(user=request.user)
    serializer = QuestionSerializer(questions, many=True)
    response_data = {
      "count":questions.count(),
      "questions": serializer.data
    }
    return Response(response_data) 
  def post(self, request, format=None):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class QuestionDetail(views.APIView):
  def get_object(self, pk):
    try:
      return Question.objects.get(pk=pk)
    except Question.DoesNotExist:
      raise Http404
    
  def get(self, request, pk, format=None):
    question = self.get_object(pk)
    serializer = QuestionSerializer(question)
    like_bool = False
    if request.user in question.like_users.all():
      like_bool = True

    response_data = {
      "like": like_bool,
      "count":question.like_users.count(),
      "question": serializer.data
    }
    return Response(response_data)

  def put(self, request, pk, format=None):
      if not request.user.is_authenticated:
        return Response({"message":"수정 권한이 없습니다."})
      question = get_object_or_404(Question, pk=pk)
        
      if question.user != request.user:
        return Response({"message":"수정 권한이 없습니다."})
      
      serializer = QuestionSerializer(question, data = request.data)
      if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def patch(self, request, pk, format=None):
    if not request.user.is_authenticated:
      return Response({"message":"수정 권한이 없습니다."})
    question = get_object_or_404(Question, pk=pk)
        
    if question.user != request.user:
      return Response({"message":"수정 권한이 없습니다."})
      
    serializer = QuestionSerializer(question, data = request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk, format=None):
    if not request.user.is_authenticated:
      return Response({"message":"삭제 권한이 없습니다."})
    question=get_object_or_404(Question, pk=pk)
    if question.user != request.user:
        return Response({"message":"삭제 권한이 없습니다."})
    
    question.delete()
    return Response({"message":"게시물 삭제 성공"})
  

  
class CommentView(views.APIView):
  def post(self, request, format=None):
    serializer=CommentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data)
    return Response(serializer.errors)
  # def put(self, request, format=None):


  # def delete(self, request, pk, format=None):

class Like(views.APIView):
  def post(self, request, pk,format=None):
    if not request.user.is_authenticated:
      return Response({"message":"로그인이 필요합니다."})
    
    question = get_object_or_404(Question, pk=pk)
    
    if request.user in question.like_users.all():
      return Response({"message":"이미 좋아요를 눌렀습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
    question.like_users.add(request.user)
    question.save()
    
    serializer = QuestionSerializer(question)

    return Response({"message":"좋아요", "data":serializer.data}, status=status.HTTP_201_CREATED)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)