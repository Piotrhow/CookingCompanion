from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import PantryIngredient, Pantry
from recipes.models import Ingredient, Recipe, RecipeIngredient


class RecipeListView(ListView):
    model = Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    search_input = request.GET.get("search_input")

    if search_input:
        recipes_filter = Recipe.objects.filter(name__contains=search_input)
        res = render(
            request,
            'recipes/recipe_list.html',
            context={
                'recipe_list': recipes_filter,
                'search_input': search_input,
            }
        )
        res.set_cookie("search_input", search_input)
        # print(search_input)
        return res

    res = render(
        request,
        'recipes/recipe_list.html',
        context={
            'recipe_list': recipes,
        }
    )
    res.delete_cookie("search_input")

    return res


def recipe_detail(request, id):
    r = get_object_or_404(Recipe, id=id)
    ri = RecipeIngredient.objects.filter(recipe_id=id)   #filter only ingredients used in this recipe

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
    r = get_object_or_404(Recipe, id=id)
    current_user = request.user
    ri = RecipeIngredient.objects.filter(recipe_id=id)  # shows ingredients used in recipe
    residual = RecipeIngredient.objects.filter(recipe_id=id)   # stores ingredients used in recipe
    pantry = Pantry.objects.filter(user__id=current_user.id)  # select current's user pantry
    pi = PantryIngredient.objects.filter(pantry__in=pantry)  # shows all ingredients of selected pantry
    partly_missing = dict()

    for recip_ingred in ri:
        pantry_ingred = pi.filter(ingredient__id=recip_ingred.ingredient.id).first()   # select ingredient from pantry
        if pantry_ingred:
            res = pantry_ingred.quantity - recip_ingred.quantity       # calculate quantity
            if res < 0:
                partly_missing[pantry_ingred.ingredient] = res * -1        # if calculated < 0 save to dict

            residual = residual.exclude(id=recip_ingred.id)          # exclude not missing ingredients

    return render(
        request,
        'recipes/recipe_check.html',
        context={
            'recipe': r,
            'recipe_ingredients': ri,
            'pantry_ingredients': pi,
            'missing_ingredients': residual,
            'partly_missing_ingredients': partly_missing,
        },
    )


@login_required()
def pantry_subtraction(request, id):
    r = get_object_or_404(Recipe, id=id)
    current_user = request.user
    ri = RecipeIngredient.objects.filter(recipe_id=id)
    pantry = Pantry.objects.filter(user__id=current_user.id)
    pi = PantryIngredient.objects.filter(pantry__in=pantry)

    # print(pantry)
    # print(pi)
    # print(ri)

    for recip_ingred in ri:
        pantry_ingred = pi.filter(ingredient__id=recip_ingred.ingredient.id).first()
        # print(recip_ingred.ingredient.id)
        # print(pantry_ingred)
        res = pantry_ingred.quantity - recip_ingred.quantity
        pantry_ingred.quantity = res
        if res >= 0:
            pantry_ingred.save()
        else:
            print("Unknown error!")

    return render(
        request,
        'recipes/pantry_subtract.html',
        context={
            'recipe': r,
            'recipe_ingredients': ri,
        }
    )

# PRINT OUT SHOPPING LIST
def recipe_shoppinglist(request, id):
    recipes = get_object_or_404(Recipe, id=id)
    current_user = request.user
    recipe_ingredients = RecipeIngredient.objects.filter(recipe_id=id)
    pantry = Pantry.objects.filter(user__id=current_user.id)
    pantry_ingredients = PantryIngredient.objects.filter(pantry__in=pantry)
    residual = RecipeIngredient.objects.filter(recipe_id=id)   # stores ingredients used in recipe

    missing = {}

    for recip_ingred in recipe_ingredients:
        pantry_ingred = pantry_ingredients.filter(ingredient__id=recip_ingred.ingredient.id).first()   # select ingredient from pantry
        if pantry_ingred:
            res = pantry_ingred.quantity - recip_ingred.quantity       # calculate quantity
            if res < 0:
                missing[pantry_ingred.ingredient] = res * -1        # if calculated < 0 save to dict
            residual = residual.exclude(id=recip_ingred.id)
            for residual_item in residual:
                missing[residual_item.ingredient] = residual_item.quantity

    print(missing)


    return render(
        request,
        'recipes/recipe_shoppinglist.html',
        context={
            'recipe': recipes,
            'missing_ingredients': missing,
        }
    )
