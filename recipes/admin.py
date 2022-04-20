from django.contrib import admin

from .models import Ingredient, IngredientCategory, IngredientUnit, Recipe, RecipeIngredient

admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
admin.site.register(IngredientUnit)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)