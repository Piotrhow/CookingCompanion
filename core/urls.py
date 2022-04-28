from django.urls import path

from core import views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
	path('pantry-detail/', views.pantry_detail, name='pantry-detail'),
	path('pantry-detail-form/', views.pantry_detail_form, name='pantry-detail-form'),
	path('create/', views.pantryingredient_create, name='create'),
	path('delete/<int:pk>/', views.pantryingredient_delete, name='delete'),
	# path('delete/<int:pk>/', views.pantryingredient_delete, name='delete-multiple'),
	path('update/<int:pk>/', views.pantryingredient_update, name='update'),
	path('check/', views.pantryingredient_check, name='pantry-check'),
]

