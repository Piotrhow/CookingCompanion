from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views
from django.urls import reverse
from urllib.parse import urlencode
from django.db import IntegrityError

from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import Pantry, PantryIngredient
from recipes.models import Ingredient, IngredientCategory

EMPTY_MSG = 'It looks like you don\'t have anything yet.'
DUPLICATE_MSG = 'Sorry... It looks like you already have that item. Try updating the existing amount instead.'
WRONG_NAME_MSG = 'Something\'s wrong. Try again and make sure you don\'t make any typos.'


# READ PANTRY VIEW - wyświetlanie widoku Pantry dla danego Usera
@login_required()
def pantry_detail(request):
	id = request.user.id
	pantry = get_object_or_404(Pantry, user_id=id)
	pantryingredients_all = PantryIngredient.objects.filter(pantry_id=pantry.id)
	categories_all = IngredientCategory.objects.all()

	# Podział pantryingredients na kategorie
	dict = {}
	for category in categories_all:
		ingredient_fits_category = pantryingredients_all.filter(ingredient__category_id=category.id)
		if ingredient_fits_category:
			dict[category.name] = ingredient_fits_category

	return render(
		request,
		'core/pantry_detail.html',
		context={
			'empty_msg': EMPTY_MSG,
			'pantry_ingredients': pantryingredients_all,
			'categories_all': categories_all,
			'ingredient_fits_category': dict,
		}
	)


# CREATE PANTRY INGREDIENT - widok dodawania elementów do Pantry
def set_cookie(param, ingredient_id):
	pass


def pantryingredient_create(request):
	id = request.user.id
	pantry = get_object_or_404(Pantry, user_id=id)
	ingredients_all = Ingredient.objects.all()
	categories_all = IngredientCategory.objects.all()

	ingredient_category = (request.GET.get('ingredient_category'))  # pobieranie od USERA
	ingredient_id = (request.GET.get('ingredient_id'))  # pobieranie od USERA

	if request.method == "POST":
		quantity = request.POST.get('quantity') #pobieranie od USERA
		try:
			PantryIngredient.objects.create(
				quantity=quantity,
				ingredient_id=ingredient_id,
				pantry_id=pantry.id,
			)
			return redirect('core:pantry-detail')
		except IntegrityError:
			integrityerror_flag = 1

		res = redirect('core:create')
		res.set_cookie("integrityerror_flag", integrityerror_flag)
		return res

	else: #Jeżeli metoda GET

		integrityerror_flag = request.COOKIES.get("integrityerror_flag", 0)
		ingredientchosen_flag = request.COOKIES.get("ingredientchosen_flag", 0)

		if integrityerror_flag:
			integrityerror_flag = int(integrityerror_flag)

		if ingredient_category:
			ingredients_all = Ingredient.objects.filter(category__name=ingredient_category)

		if ingredientchosen_flag:
			ingredientchosen_flag = int(ingredientchosen_flag)

		ingredient = request.COOKIES.get("ingredient", 0)
		if ingredient_id:
			ingredientchosen_flag = 1
			ingredient = Ingredient.objects.get(id=ingredient_id)


		res = render(
			request,
			'core/pantryingredient_form.html',
			context={
				'empty_msg': EMPTY_MSG,
				'duplicate_msg': DUPLICATE_MSG,
				'wrong_name_msg': WRONG_NAME_MSG,
				'integrityerror_flag': integrityerror_flag,
				'ingredientchosen_flag': ingredientchosen_flag,
				'categories_all': categories_all,
				'ingredients_all': ingredients_all,
				'ingredient': ingredient,
			}
		)

		res.delete_cookie("integrityerror_flag")
		res.delete_cookie("ingredientchosen_flag")
		res.delete_cookie("ingredient")

		return res


# DELETE AN INGREDIENT - usuwanie wybranego składnika z pantry
def pantryingredient_delete(request, pk):
	pantryingredient = get_object_or_404(PantryIngredient, pk=pk)
	ingredient = get_object_or_404(Ingredient, id=pantryingredient.ingredient_id)

	if request.method == "POST":
		pantryingredient.delete()
		return redirect('core:pantry-detail')

	return render(
		request,
		'core/confirm_delete.html',
		context={
			'pantryingredient': pantryingredient,
			'ingredient': ingredient,
		}
	)

# UPDATE AN INGREDIENT AMOUNT - modyfikowanie wybranego składnika z pantry
def pantryingredient_update(request, pk):
	pantryingredient = get_object_or_404(PantryIngredient, pk=pk)
	ingredient = get_object_or_404(Ingredient, id=pantryingredient.ingredient_id)
	quantity_old = pantryingredient.quantity
	modified_pi = request.POST.get("quantity") #pobieranie od usera

	if modified_pi:
		pantryingredient.quantity = modified_pi
		pantryingredient.save()
		return redirect('core:pantry-detail')

	return render(
		request,
		'core/pantryingredient_form_update.html',
		context={
			'ingredient': ingredient,
			'quantity_old': quantity_old,
		}
	)


# READ PANTRY VIEW - WITH CHECKBOXES AND FORM
def pantry_detail_form(request):
	id = request.user.id
	p = get_object_or_404(Pantry, user_id=id)
	pantry_id = p.id
	pi_all = PantryIngredient.objects.filter(pantry_id=pantry_id)
	categories_all = IngredientCategory.objects.all()
	ingredients = Ingredient.objects.all()

	if request.method == "POST":
		ingredients_chosen = (request.POST.getlist('ingredients_check[]'))  # pobieranie od usera
		# print(ingredients_chosen)
		for ingredient_chosen in ingredients_chosen:
			# print(ingredient_chosen)
			p = PantryIngredient.objects.get(pk=ingredient_chosen)
			print(p)
		base_url = reverse('core:pantry-check')
		query_list = urlencode({'ingredients_chosen': ingredients_chosen})
		url = '{}?{}'.format(base_url, query_list)
		return redirect(url)

	print(request.POST)
	ingredients_chosen = (request.GET.get('ingredients_check[]'))  # pobieranie od usera

	# if ingredients_chosen:
	# 	array = []
	# 	for ingredient_chosen in ingredients_chosen:
	# 		p = PantryIngredient.objects.get(pk=ingredient_chosen)
	# 		array.append(p)
	# 	print(array)
	# 	return render(
	# 		request,
	# 		'core/pantry_check.html',
	# 		context={
	# 			'ingredients': ingredients,
	# 			'pantry_ingredients': array,
	# 		}
	# 	)

	dict = {}
	for category in categories_all:
		ingredient_fits_category = pi_all.filter(ingredient__category_id=category.id)
		if ingredient_fits_category:
			dict[category.name] = ingredient_fits_category

	return render(
		request,
		'core/pantry_detail_form.html',
		context={
			'pantry_ingredients': pi_all,
			'empty_msg': EMPTY_MSG,
			'categories_all': categories_all,
			'ingredient_fits_category': dict,
		}
	)


# CHECK AND COMPARE PANTRYINGREDIENTS WITH RECIPES
def pantryingredient_check(request):
	ingredients_chosen = request.GET.getlist('p')

	# for ingredient_chosen in ingredients_chosen:
	# 	print(ingredient_chosen)

	return render(
		request,
		'core/pantry_check.html',
		context={
			# 'pantryingredient': pi,
			# 'ingredient': ingredient,
			'ingredients_chosen': ingredients_chosen,
			'pantry_ingredients': 'array',
		}
	)
