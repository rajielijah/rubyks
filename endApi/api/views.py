from rest_framework.generics import CreateAPIView
#from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, ChangePasswordSerializer, LoginSerializer, RegisterSerializer, ProfileSerializer, PostSerializer
from endApi.models import Profile, Post, User
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.contrib.auth import login 
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.decorators import login_required
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer        

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })        


class ProfileView(viewsets.ModelViewSet):
    lookup_field = 'id' 
    queryset = Profile.objects.all()
    serializer_class =ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)


# class UserList(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class =UserSerializer
#     permission_classes = (permissions.AllowAny,)

# class UserDetail(RetrieveAPIView):
#     lookup_field = 'username'
#     queryset = User.objects.all()
#     serializer_class =UserSerializer
#     permission_classes = (permissions.AllowAny,)

class PostView(viewsets.ModelViewSet):    
    lookup_field = 'id' 
    queryset = Post.objects.all()
    serializer_class =PostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
    pagination_class = PageNumberPagination


class UserView(viewsets.ModelViewSet):
    lookup_field = 'username' 
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
