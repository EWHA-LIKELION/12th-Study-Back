from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class QuestionList(views.APIView):
    def get(self, request, format=None):
        questions = Question.objects.filter(user=self.request.user)

        keyword = request.GET.get('keyword', None)
        if keyword:
            questions = questions.filter(title__icontains=keyword)

        order = request.GET.get('order', '최신순')  
        if order == '오래된순':
            questions = questions.order_by('date')
        else:
            questions = questions.order_by('-date')

        serializer = QuestionSerializer(questions, many=True)
        return Response({"count": questions.count(), "questions": serializer.data})
    
    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuestionDetail(views.APIView):
    def get_object(self, pk):
        try:
            question = Question.objects.get(pk=pk)
            if question.user != self.request.user:
                raise Http404
            return question
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        liked = question.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
        serializer = QuestionSerializer(question, context={'request': request})
        data = serializer.data
        data['liked'] = liked 
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Ensure the user is set correctly
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Ensure the user is set correctly
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response({"message": "게시물 삭제 성공"}, status=status.HTTP_204_NO_CONTENT)

class AnswerView(views.APIView):
    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AnswerDetail(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Answer, pk=pk)

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        liked = answer.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
        serializer = AnswerSerializer(answer, context={'request': request})
        data = serializer.data
        data['liked'] = liked 
        return Response(data)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Ensure the user is set correctly
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Ensure the user is set correctly
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        answer = self.get_object(pk)
        answer.delete()
        return Response({"message": "답변 삭제 성공"}, status=status.HTTP_204_NO_CONTENT)


class QuestionLikeAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({'error': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if question.likes.filter(id=request.user.id).exists():
            return Response({'message': 'You already liked this question'}, status=status.HTTP_400_BAD_REQUEST)
        
        question.likes.add(request.user)
        return Response({'message': 'Question liked successfully'}, status=status.HTTP_201_CREATED)

class AnswerLikeAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return Response({'error': 'Answer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # 로직: 해당 유저가 이미 좋아요를 눌렀는지 확인하고, 없으면 추가
        if answer.likes.filter(id=request.user.id).exists():
            return Response({'message': 'You already liked this answer'}, status=status.HTTP_400_BAD_REQUEST)
        
        answer.likes.add(request.user)
        return Response({'message': 'Answer liked successfully'}, status=status.HTTP_201_CREATED)