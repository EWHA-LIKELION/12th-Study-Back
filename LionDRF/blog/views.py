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
    if category:
      questions = Question.objects.filter(category__icontains=category)
    else:
      questions = Question.objects.all()
    if order == "desc":
      questions=questions.order_by('-upload_time')
    serializer = QuestionSerializer(questions, many=True)
    response_data = {
      "count":Question.objects.count(),
      "questions": serializer.data
    }
    return Response(response_data) 
  def post(self, request, format=None):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
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
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    question = self.get_object(pk)
    serializer = QuestionSerializer(question, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk, format=None):
    question=get_object_or_404(Question, pk=pk)
    question.delete()
    return Response({"message":"게시물 삭제 성공"})
  
