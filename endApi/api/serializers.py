from django.contrib.auth.models import User
from rest_framework import serializers
from endApi.models import  Profile, Post
from django.core.paginator import Paginator
from rest_framework.settings import api_settings
from django.contrib.auth import authenticate
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer


class LoginSerializer(RestAuthLoginSerializer):
    username = None
<<<<<<< HEAD

=======
>>>>>>> afaa8063c1634982e92cde53f88b3879c458d652


class SocialSerializer(serializers.Serializer):
    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'company_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        email = self.validated_data['email']
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise serializers.ValidationError(
                'This e-mail has already been used by another user'
            )

        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], password=validated_data['password'])
        # user.first_name = self.validated_data['first_name']
        # user.last_name = self.validated_data['last_name']
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Details")

    def create(self, validated_data):
        email = self.validated_data['email']

        user = User.objects.create_user(
            validated_data['email'], password=validated_data['password'])
        # user.first_name = self.validated_data['first_name']
        # user.last_name = self.validated_data['last_name']
        user.save()
        return user

class AuthorPostSerializer(serializers.ModelSerializer):
    # company_name = serializers.SlugRelatedField(read_only=True, slug_field='company_name')
    class Meta:
        model = Profile
        fields = ('id', 'avatar','name')

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Profile
        fields = ('id', 'avatar', 'name', 'phone', 'whatsapp', 'bio', 'gender', 'location', 'state',  'user' )


class PostSerializer(serializers.ModelSerializer):   
    author  = AuthorPostSerializer(read_only=True)
    class Meta:
        model  = Post
        fields = ( 'id', 'author',  'category', 'product_name', 'price','product_description', 'product_details',  'image', 'posted_on')


<<<<<<< HEAD
    def create(self, validated_data):

        author_data = validated_data.pop('author')
        author = AuthorPostSerializer.create(AuthorPostSerializer(), validated_data=author_data)
        detail, created = Post.objects.update_or_create(author=author,
                        subject_major=validated_data.pop('subject_major'))
        return detail
=======
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
>>>>>>> afaa8063c1634982e92cde53f88b3879c458d652

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
