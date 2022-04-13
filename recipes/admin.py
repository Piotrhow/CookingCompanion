from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, IngredientUnit, IngredientCategory

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(IngredientUnit)
admin.site.register(IngredientCategory)
