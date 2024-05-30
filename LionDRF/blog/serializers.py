from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from blog.models import Question, Comment
from api.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields=['id','post', 'username', 'comment_text','created_at']

class QuestionSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['id', 'title', 'date', 'body', 'language', 'liked']
    
    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
    
    def create(self, data):
        user=User.objects.create(
            email=data['email'],
            username=data['username'],
        )
        user.set_password(data['password'])
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    email= serializers.CharField(max_length=64)
    password= serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email=data.get('email',None)
        password=data.get('password',None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'id': user.id,
                    'email': user.email ,
                    'access_token': access
                }
                return data
