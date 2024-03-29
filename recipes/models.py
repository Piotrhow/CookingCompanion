from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class Recipe(models.Model):
	name = models.CharField(max_length=128, unique=True)
	description = models.TextField()
	added = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	picture = models.ImageField(default='recipe_def.jpg', upload_to='recipe_images')
	ingredients = models.ManyToManyField(
		'Ingredient',
		through='RecipeIngredient',
		through_fields=('recipe', 'ingredient'),
	)
	# DODATKOWE
	# tags = models.ManyToMany(...) #jako osobna apka??
	# likes = models.PositiveIntegerField() #jako zlicznie ilosci lajkow
	# rating = models.PositiveIntegerField(min_value=1, max_value=5) #jako rating

	def __str__(self):
		return f'{self.name}'

	# # resizing images - WYŁĄCZONE
	# def save(self, *args, **kwargs):
	# 	super().save()
	#
	# 	img = Image.open(self.picture.path)
	#
	# 	if img.height > 250 or img.width > 250:
	# 		new_img = (250, 250)
	# 		img.thumbnail(new_img)
	# 		img.save(self.picture.path)


class Ingredient(models.Model):
	name = models.CharField(max_length=128, unique=True)
	unit = models.ForeignKey('IngredientUnit', on_delete=models.SET_NULL, blank=True, null=True)
	category = models.ForeignKey('IngredientCategory', on_delete=models.SET_NULL, blank=True, null=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return f'{self.name} ({self.unit})'


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
	ingredient = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.DecimalField(max_digits=7, decimal_places=2)

	class Meta:
		unique_together = [['recipe', 'ingredient']]

	def __str__(self):
		return f'{self.ingredient} {self.quantity}'


class IngredientUnit(models.Model):
	name = models.CharField(max_length=64, unique=True)

	def __str__(self):
		return self.name


class IngredientCategory(models.Model):
	name = models.CharField(max_length=64, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Ingredient categories"
		ordering = ['name']
