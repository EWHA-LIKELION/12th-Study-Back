from rest_framework import serializers
from blog.models import Question, Answer, LANGUAGE_CHOICES
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username' , 'email']

class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes = serializers.StringRelatedField(many=True, required=False)
    likes_count = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_liked_by_user(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False

    class Meta:
        model= Answer
        fields=['id', 'question' ,'user','answer_text','created_at', 'likes_count' , 'likes', 'liked_by_user']

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    likes = serializers.StringRelatedField(many=True, required=False)
    likes_count = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()
    answers = AnswerSerializer(many= True, read_only = True)

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_liked_by_user(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'user', 'date', 'body', 'language', 'answers', 'likes_count' , 'likes', 'liked_by_user']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    




