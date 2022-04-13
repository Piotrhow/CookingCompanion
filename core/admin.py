from django.contrib import admin

from .models import Pantry, PantryIngredient, PantryUserTest

admin.site.register(Pantry)
admin.site.register(PantryIngredient)
admin.site.register(PantryUserTest)
