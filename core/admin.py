from django.contrib import admin

from .models import Pantry, PantryIngredient

admin.site.register(Pantry)
admin.site.register(PantryIngredient)

