from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import *
from .serializers import *

# Create your views here.
class SignUpView(views.APIView):
  def post(self, request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message':'회원가입 성공', 'data':serializer.data})
    return Response({'message': '회원가입 실패', 'error':serializer.errors})
  
class LoginView(views.APIView):
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)

    if serializer.is_valid():
      return Response({"message":"로그인 성공", "data":serializer.validated_data})
    return Response({"message": "로그인 실패", 'error':serializer.errors})