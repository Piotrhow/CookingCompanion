from django.db import models
# from accounts.models import User
from recipes.models import Ingredient


# Create your models here.
class Pantry(models.Model):
	added = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	pantryusertest = models.OneToOneField('PantryUserTest', on_delete=models.CASCADE)  # relacja z userem !!!
	ingredients = models.ManyToManyField(
		Ingredient,
		through='PantryIngredient',
		through_fields=('pantry', 'ingredient'),
	)

	def __str__(self):
		return f'Pantry of {self.pantryusertest}'

	class Meta:
		verbose_name_plural = "Pantries"


class PantryIngredient(models.Model):
	pantry = models.ForeignKey('Pantry', on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return f'{self.pantry}: {self.ingredient} {self.quantity}'


class PantryUserTest(models.Model):  # do_usuniecia_po zmergowaniu accounts
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return f'User {self.pk}'