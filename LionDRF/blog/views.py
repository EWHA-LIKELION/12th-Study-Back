from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *

# Create your views here.
class QuestionList(views.APIView):
    def get(self, request, format=None):
        post=Question.objects.all()
        keyword= request.GET.get('keyword', None)
        if keyword:
            post= Question.objects.filter(title__icontains=keyword)
        else:
            post= Question.objects.all()
        
        post=post.order_by('-date')
        serializer= QuestionSerializer(post, many=True)
        response_data={
            "count": post.count(),
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
        post = self.get_object(pk)
        serializer = QuestionSerializer(post)
        return Response(serializer.data)
   
    def put(self, request, pk, format=None):
        post=get_object_or_404(Question, pk=pk)
        serializer=QuestionSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        post=get_object_or_404(Question, pk=pk)
        post.delete()
        return Response({"message":"질문 삭제 성공"})