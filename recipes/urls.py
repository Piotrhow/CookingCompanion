from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('recipe-list/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe-detail'),
    path('recipe-check/<int:id>', views.recipe_check, name='recipe-check'),
    path('pantry_subtract/<int:id>', views.pantry_subtraction, name='pantry-subtract'),
    # path('recipe/shoppinglist/', views.recipe_shoppinglist, name='recipe-shoppinglist'),
    ]
