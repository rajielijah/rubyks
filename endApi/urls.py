from django.urls import path
from .api import views 
from rest_framework.authtoken.views import obtain_auth_token 
from knox import views as knox_views
from django.urls import path, include, re_path
from rest_framework import routers
from .api.views import ProfileView, SocialLoginView, PostView, RegisterAPI, UserView, ChangePasswordView
from rest_auth.views import PasswordResetConfirmView

router = routers.SimpleRouter()
router.register(r'profile', ProfileView, 'userprofile')
router.register(r'user', UserView, 'userdelete')
router.register(r'post', PostView, 'post')

    

urlpatterns = [
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
        path('api/register/', RegisterAPI.as_view(), name='register'),
        path('api/login/', views.LoginAPI.as_view(), name='account_login'),
        path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
        path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
        path('', include(router.urls)),
        path('rest/', include('rest_auth.urls')),
        re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
        path('rest/register/', include('rest_auth.registration.urls')),
        path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
        path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
        path('oauth/login/', SocialLoginView.as_view()),
        path('accounts/', include('allauth.socialaccount.providers.facebook.urls'))
]       