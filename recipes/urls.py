from django.urls import path

from recipes import views
from django.views.generic import TemplateView

app_name = 'recipes'

urlpatterns = [
	path('recipe-list/', views.RecipeListView.as_view(), name='recipe-list'),
	path('recipe/<int:id>/', views.recipe_detail, name='recipe-detail'),
	path('recipe-check/', views.recipe_check, name='recipe-check'),
    #
    #
]