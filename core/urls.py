from django.urls import path

from core import views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
	path('pantry-detail/', views.pantry_detail, name='pantry-detail'),
	path('create/', views.pantryingredient_create, name='create'),
	path('delete/<int:pk>/', views.pantryingredient_delete, name='delete'),
	path('update/<int:pk>/', views.pantryingredient_update, name='update'),
]

