from django.shortcuts import render, get_list_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import Question
from .serializers import QuestionSerializer

# Create your views here.


class QuestionList(views.APIView):
    def get(self, request, format=None):
        keyword = request.GET.get('keyword', None)
        sort_option = request.GET.get('sort', None)

        if keyword:
            questions = Question.objects.filter(title__icontains=keyword)
        else:
            questions = Question.objects.all()
        print(sort_option)
        if sort_option == 'latest':
            questions = questions.order_by('-date')  # 최신순 정렬
        elif sort_option == 'oldest':
            questions = questions.order_by('date')   # 오래된순 정렬
        elif sort_option == 'string':
            questions = questions.order_by('title')  # 제목순 정렬
        else:
            questions = questions.order_by('-date')  # 기본 최신순 정렬

        count = questions.count()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"count": count, "questions": serializer.data})

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
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response({"message": "게시물 삭제 성공"})
