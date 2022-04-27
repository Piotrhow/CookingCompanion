from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import PantryIngredient, Pantry
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


@login_required()
def recipe_check(request, id):
    current_user = request.user
    ri = RecipeIngredient.objects.filter(recipe_id=id)  # shows ingredients used in recipe
    residual = RecipeIngredient.objects.filter(recipe_id=id)  # shows ingredients used in recipe
    pantry = Pantry.objects.filter(user__id=current_user.id)  # select current's user pantry
    pi = PantryIngredient.objects.filter(pantry__in=pantry)  # shows all ingredients of selected pantry
    partly_missing = dict()

    for recip_ingred in ri:
        pantry_ingred = pi.filter(ingredient__id=recip_ingred.ingredient.id).first()
        if pantry_ingred:
            res = pantry_ingred.quantity - recip_ingred.quantity
            if res < 0:
                partly_missing[pantry_ingred.ingredient] = res * - 1
            residual = residual.exclude(id=recip_ingred.id)
    print(residual)



    return render(
        request,
        'recipes/recipe_check.html',
        context={
            'recipe_ingredients': ri,
            'pantry_ingredients': pi,
            'missing_ingredients': residual,
            'partly_missing_ingredients': partly_missing,
        },

    )


@login_required()
def pantry_subtract(request):
    return render(request,'recipes/pantry_subtract.html')