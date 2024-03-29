from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db import IntegrityError

from core.models import Pantry, PantryIngredient
from recipes.models import Ingredient, IngredientCategory, Recipe, RecipeIngredient

EMPTY_MSG = 'It looks like you don\'t have anything yet.'
DUPLICATE_MSG = 'Sorry... It looks like you already have that item. Try updating the existing amount instead.'
WRONG_NAME_MSG = 'Something\'s wrong. Try again and make sure you don\'t make any typos.'
CHOOSE_STH_MSG = 'Oops, looks like you didn\'t choose  anything...'

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
			dict[category] = ingredient_fits_category

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
		'core/pantry_delete_confirm.html',
		context={
			'pantryingredient': pantryingredient,
			'ingredient': ingredient,
		}
	)


# DELETE CATEGORY INGREDIENTS - usuwanie wszystkich składnikw z DANEJ KATEGORII
def pantryingredient_delete_category(request, pk):
	category = get_object_or_404(IngredientCategory, pk=pk)
	pantryingredients = PantryIngredient.objects.filter(ingredient__category__id=pk)

	if request.method == "POST":
		pantryingredients.delete()
		return redirect('core:pantry-detail')

	return render(
		request,
		'core/pantry_delete_confirm_category.html',
		context={
			'pantryingredients': pantryingredients,
			'category': category,
		}
	)


# DELETE PANTRY INGREDIENTS - usuwanie wszystkich składnikw z PANTRY
def pantryingredient_delete_pantry(request):
	id = request.user.id
	pantry = get_object_or_404(Pantry, user_id=id)
	pantryingredients = PantryIngredient.objects.filter(pantry=pantry.id)

	if request.method == "POST":
		pantryingredients.delete()
		return redirect('core:pantry-detail')

	return render(
		request,
		'core/pantry_delete_confirm_pantry.html',
		context={
			'pantryingredients': pantryingredients,
			'pantry': pantry,
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
	pantry = get_object_or_404(Pantry, user_id=id)
	pantryingredients_all = PantryIngredient.objects.filter(pantry_id=pantry.id)
	categories_all = IngredientCategory.objects.all()
	choose_sth_msg = request.COOKIES.get("choose_sth_msg", 0)

	# POBIERANIE Z CHECKBOX'ÓW LISTY ID - przekazane na następny widok metodą POST
	if request.method == "POST":
		# try:
		ingredients_chosen = (request.POST.getlist('ingredients_check[]'))  # pobieranie od usera
		if ingredients_chosen:
			res = redirect('core:pantry-check')
			res.set_cookie("ingredients_chosen", ingredients_chosen)
			return res

		# except ValueError:
		# 	valueerror_flag = 1

		res = redirect('core:pantry-detail-form')
		choose_sth_msg = res.set_cookie("choose_sth_msg", CHOOSE_STH_MSG)
		return res

	else:
		# pantryingredients to category
		dict = {}
		for category in categories_all:
			ingredient_fits_category = pantryingredients_all.filter(ingredient__category_id=category.id)
			if ingredient_fits_category:
				dict[category.name] = ingredient_fits_category

		res = render(
			request,
			'core/pantry_detail_form.html',
			context={
				'empty_msg': EMPTY_MSG,
				'choose_sth_msg': choose_sth_msg,
				'pantry_ingredients': pantryingredients_all,
				'categories_all': categories_all,
				'ingredient_fits_category': dict,
			}
		)

		res.delete_cookie("ingredients_chosen")
		res.delete_cookie("valuerror_flag")
		res.delete_cookie("choose_sth_msg")

		return res


# CHECK AND COMPARE PANTRYINGREDIENTS WITH RECIPES
def pantryingredient_check(request):
	recipes_all = Recipe.objects.all()
	ingredients_chosen = request.COOKIES.get("ingredients_chosen", 0)

	# cleaning list
	x = ingredients_chosen.replace("[]","")
	x = x.replace("']","")
	x = x.replace("['","")
	x = x.replace("', '", " ")
	ingredients_chosen = x.split()

	# make checkbox list
	array = []
	for id in ingredients_chosen:
		ingredient_chosen = PantryIngredient.objects.get(id=id)
		array.append(ingredient_chosen)
	ingredients_chosen = array

	matching = dict()
	for recipe in recipes_all:
		recipe_matching = 0
		recipe_ingredients = RecipeIngredient.objects.filter(recipe_id=recipe.id)
		for recipe_ingredient in recipe_ingredients:
			for ingredient_chosen in ingredients_chosen:
				if ingredient_chosen.ingredient.id == recipe_ingredient.ingredient.id:
					recipe_matching += 1
					if ingredient_chosen.quantity >= recipe_ingredient.quantity:
						recipe_matching += 1
					else:
						recipe_matching -= 1
				else:
					continue
		matching[recipe] = recipe_matching

	sorted_values = sorted(matching.values(), reverse=True)  # sort dict from high to low
	sorted_recipes = {}

	for i in sorted_values:
		for key in matching.keys():
			if matching[key] == i and matching[key] > 0:
				sorted_recipes[key] = matching[key]

	return render(
		request,
		'core/pantry_check.html',
		context={
			'recipes_all': recipes_all,
			'ingredients_chosen': ingredients_chosen,
			'sorted_recipes': sorted_recipes,
		},
	)


