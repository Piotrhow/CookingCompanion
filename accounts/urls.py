from django.urls import path, include, re_path
from .views import home, RegisterView, ResetPasswordView
from django.contrib.auth import views as auth_views

from accounts.views import CustomLoginView
from accounts.forms import LoginForm
from .views import profile

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='register'),
    # redirect_authenticated_user=True means that users who try to access the login page
    # after they are authenticated will be redirected back.
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    path('/profile/', profile, name='users-profile'),
]


