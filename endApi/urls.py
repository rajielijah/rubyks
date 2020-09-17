from django.urls import path
from .api import views 
from rest_framework.authtoken.views import obtain_auth_token 
from knox import views as knox_views
from django.urls import path, include
from rest_framework import routers
from .api.views import ProfileView, PostView, RegisterAPI, UserView, ChangePasswordView, LoginAPIView

router = routers.SimpleRouter()
router.register(r'profile', ProfileView, 'userprofile')
router.register(r'api/user', UserView, 'userdelete')
router.register(r'post', PostView, 'post')

    

urlpatterns = [
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
        path('api/register/', RegisterAPI.as_view(), name='register'),
        path('login/', LoginAPIView.as_view(), name='login'),
        path('api/login/', views.LoginAPI.as_view()),
        path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
        path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
        path('', include(router.urls)),
        path('rest/', include('rest_auth.urls')),
        path('rest/register/', include('rest_auth.registration.urls')),
        path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
        path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    #    path('user/', UserList.as_view(), name='userlist'),
]       