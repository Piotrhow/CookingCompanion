from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views
from django.db import IntegrityError

from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import Pantry, PantryIngredient
from recipes.models import Ingredient, IngredientCategory

EMPTY_MSG = 'It looks like you don\'t have anything yet.'
DUPLICATE_MSG = 'It looks like you already have that item. Try updating the existing amount instead.'

# Create your views here.
def pantry_detail(request):

	if request.user.is_authenticated:
		id = request.user.id
		p = get_object_or_404(Pantry, user_id=id)
		print(f"Username --> {request.user.username}")
	else:
		return redirect('/login')

	pantry_id = p.id
	pi = PantryIngredient.objects.filter(pantry_id=pantry_id)
	# ingredient_category = IngredientCategory.objects.all()
	ingredients = Ingredient.objects.all()
	print(ingredients)

	return render(
		request,
		'core/pantry_detail.html',
		context={
			'pantry': p,
			'pantry_ingredients': pi,
			'id': id,
			'empty_msg': EMPTY_MSG,
			# 'ingredient_category': ingredient_category,
			'ingredients': ingredients,
		}
	)


# CREATE PANTRY INGREDIENT
def pantryingredient_create(request):
	# ingredient_category = (request.POST.get('ingredient_category')) #pobieranie od usera
	ingredient_name = (request.POST.get('ingredient_name')) #pobieranie od usera
	quantity = request.POST.get('quantity') #pobieranie od usera
	id = request.user.id

	p = get_object_or_404(Pantry, user_id=id)
	pantry_id = p.id
	pi = PantryIngredient.objects.filter(pantry_id=pantry_id)
	flag = 0
	ingredients = Ingredient.objects.all()
	print(ingredients)

	if ingredient_name and quantity:
		ingredient = Ingredient.objects.filter(name=ingredient_name.lower()).first()
		# category = IngredientCategory.objects.filter(name=ingredient_category.lower()).first()
		ingredient_id = ingredient.id
		# category_id = category.id
		try:
			PantryIngredient.objects.create(
			pantry_id=pantry_id,
			quantity=quantity,
			ingredient_id=ingredient_id,
			)
			return redirect('core:pantry-detail')
		except IntegrityError:
			flag = 1

	return render(
		request,
		'core/pantryingredient_form.html',
		context={
			'pantry': p,
			'pantry_ingredients': pi,
			'id': id,
			'empty_msg': EMPTY_MSG,
			'duplicate_msg': DUPLICATE_MSG,
			'flag': flag,
			'ingredients': ingredients,
		}
	)

# DELETE
def pantryingredient_delete(request, pk):
	pi = PantryIngredient.objects.filter(pk=pk)

	if request.method == "POST":
		pi.delete()
		return redirect('core:pantry-detail')

	return render(
		request,
		'core/confirm_delete.html',
		context={
			'pantryingredient': pi,
		}
	)

