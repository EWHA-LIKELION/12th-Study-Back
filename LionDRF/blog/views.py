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
        #자신이 쓴 질문, 답변 조회
        mypost =request.GET.get('mypost',None)
        if mypost:
            user = request.user
            post= Question.objects.filter(user=user)

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
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionDetail(views.APIView):
    def post(self,request, pk, format=None):
        post = self.get_object(pk)
        user = request.user

        # 사용자가 이미 해당 질문을 좋아요 했는지 확인
        if post.likes.filter(id=user.id).exists():
            return Response({"message": "이미 좋아요를 눌렀습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        post.likes.add(user)
        post.save()
        serializer = QuestionSerializer(post, context={'request': request})
        return Response({"message": "좋아요 성공!", "question": serializer.data})
    
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = QuestionSerializer(post, context={'request': request})
       
        response_data = {
            "question": serializer.data,
        }
        return Response(serializer.data)
   
    def put(self, request, pk, format=None):
        post=get_object_or_404(Question, pk=pk)
        if post.user != request.user:
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        else:
            serializer=QuestionSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        post=get_object_or_404(Question, pk=pk)
        if post.user != request.user:
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        post.delete()
        return Response({"message":"질문 삭제 성공"})
    
class CommentView(views.APIView):
    def post(self,request,format=None):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

