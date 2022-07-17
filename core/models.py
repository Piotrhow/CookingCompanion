from django.db import models

from recipes.models import Ingredient
from django.contrib.auth.models import User


# Create your models here.
class Pantry(models.Model):
	added = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)  # relacja z USEREM
	ingredients = models.ManyToManyField(
		Ingredient,
		through='PantryIngredient',
		through_fields=('pantry', 'ingredient'),
	)

	def __str__(self):
		return f'Pantry of {self.user}'

	class Meta:
		verbose_name_plural = "Pantries"


class PantryIngredient(models.Model):
	pantry = models.ForeignKey('Pantry', on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		unique_together = [['pantry', 'ingredient']]

	def __str__(self):
		return f'{self.ingredient} {self.quantity}'


