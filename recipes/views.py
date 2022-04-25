from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views

from django.views.generic import CreateView, DetailView, ListView, TemplateView

from recipes.models import Ingredient, Recipe, RecipeIngredient


class RecipeListView(ListView):
	model = Recipe


def recipe_detail(request, id):

	r = get_object_or_404(Recipe, id=id)
	ri = RecipeIngredient.objects.filter(recipe_id=id)

	return render(
		request,
		'recipes/recipe_detail.html',
		context={
			'recipe': r,
			'recipe_ingredients': ri,
		}
	)


def recipe_check(request):

	if request.user.is_authenticated:
		r = get_object_or_404(Recipe, id=2)
	else:
		return redirect('/login')

	ri = RecipeIngredient.objects.filter(recipe_id=2)

	return redirect('/') #NA RAZIE PRZEKIEROWANIE NA HOME


	# return render(
	# 	request,
	# 	'recipes/recipe_check.html',
	# 	context={
	# 		'recipe': r,
	# 		'recipe_ingredients': ri,
	# 	}
	# )



