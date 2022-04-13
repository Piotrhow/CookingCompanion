from django.urls import path, include, re_path
from .views import home, RegisterView
from django.contrib.auth import views as auth_views


from accounts.views import CustomLoginView
from accounts.forms import LoginForm



urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='register'),
    # redirect_authenticated_user=True means that users who try to access the login page
    # after they are authenticated will be redirected back.
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]


