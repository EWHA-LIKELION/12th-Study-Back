from django.shortcuts import render , get_object_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *
# Create your views here.
class QuestionList(views.APIView):
    def get(self, request, format=None):
        question = Question.objects.all()
        keyword = request.GET.get('keyword', None)
        if keyword:
            question = Question.objects.filter(title__icontains=keyword)
        else:
            question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response({"count":Question.objects.count(), "question": serializer.data})
    

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionDetail(views.APIView):
    def get_object(self,pk):
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

    def patch(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BED_REQUST)
    
    def delete(self, request, pk, format=None):
        question = get_object_or_404(Question,pk=pk)
        question.delete()
        return Response({"message":"게시물 삭제 성공"})

