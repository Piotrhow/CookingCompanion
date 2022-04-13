from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('register/', views.register_page, name='register_page'),
    path('register/thanks', views.thanks_page, name='thanks_page'),
    # path('login/', views.login_page, name='login_page'),
]
