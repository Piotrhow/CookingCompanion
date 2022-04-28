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


# READ PANTRY VIEW
def pantry_detail(request):

	if request.user.is_authenticated:
		id = request.user.id
		p = get_object_or_404(Pantry, user_id=id)
	else:
		return redirect('/login')

	pantry_id = p.id
	pi_all = PantryIngredient.objects.filter(pantry_id=pantry_id)
	categories_all = IngredientCategory.objects.all()

	dict = {}
	for category in categories_all:
		ingredient_fits_category = pi_all.filter(ingredient__category_id=category.id)
		if ingredient_fits_category:
			dict[category.name] = ingredient_fits_category

	return render(
		request,
		'core/pantry_detail.html',
		context={
			'pantry_ingredients': pi_all,
			'empty_msg': EMPTY_MSG,
			'categories_all': categories_all,
			'ingredient_fits_category': dict,
		}
	)


# CREATE PANTRY INGREDIENT
def pantryingredient_create(request):
	id = request.user.id
	p = get_object_or_404(Pantry, user_id=id)
	pantry_id = p.id

	ingredients = Ingredient.objects.all()
	categories_all = IngredientCategory.objects.all()

	ingredient_category = (request.GET.get('ingredient_category'))  # pobieranie od usera
	ingredient_name = (request.GET.get('ingredient_name'))  # pobieranie od usera


	if request.method == "POST":
		quantity = request.POST.get('quantity') #pobieranie od usera

		if quantity:
			ingredient_name_list = str(ingredient_name).split()
			ingredient_name_list = ingredient_name_list[:-1]

			ingredient_name = ''
			for i in range(0, len(ingredient_name_list)):
				if i == 0:
					ingredient_name += ingredient_name_list[i]
				else:
					ingredient_name += ' ' + ingredient_name_list[i]

			ingredient = Ingredient.objects.filter(name=ingredient_name.lower()).first()

			try:
				ingredient_id = ingredient.id
				PantryIngredient.objects.create(
					pantry_id=pantry_id,
					quantity=quantity,
					ingredient_id=ingredient_id,
				)
				return redirect('core:pantry-detail')
			except IntegrityError:
				flag = 1

			res = redirect('core:create')
			res.set_cookie("flag", flag)
			return res

	else: #Jeżeli GET

		flag = request.COOKIES.get("flag", 0)
		flag1 = 0

		if flag:
			flag = int(flag)

		if ingredient_category:
			ingredients = Ingredient.objects.filter(category__name=ingredient_category)

		if ingredient_name:
			flag1 = 1

		res = render(
			request,
			'core/pantryingredient_form.html',
			context={
				'categories_all': categories_all, #jeżeli nie będzie tego - to nie pokaże listy
				'empty_msg': EMPTY_MSG,
				'duplicate_msg': DUPLICATE_MSG,
				'wrong_name_msg': WRONG_NAME_MSG,
				'flag': flag,
				'flag1': flag1,
				'ingredients': ingredients,
				'ingredient_name': ingredient_name,
			}
		)

		res.delete_cookie("flag")

		return res


# DELETE AN INGREDIENT
def pantryingredient_delete(request, pk):
	pi = get_object_or_404(PantryIngredient, pk=pk)
	ingredient = get_object_or_404(Ingredient, id=pi.ingredient_id)

	if request.method == "POST":
		pi.delete()
		return redirect('core:pantry-detail')

	return render(
		request,
		'core/confirm_delete.html',
		context={
			'pantryingredient': pi,
			'ingredient': ingredient,
		}
	)

# UPDATE AN INGREDIENT AMOUNT
def pantryingredient_update(request, pk):
	pi = get_object_or_404(PantryIngredient, pk=pk)
	ingredient = get_object_or_404(Ingredient, id=pi.ingredient_id)
	quantity_old = pi.quantity
	modified_pi = request.POST.get("quantity") #pobieranie od usera

	if modified_pi:
		pi.quantity = modified_pi
		pi.save()
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

	# if request.method == "POST":
	# 	ingredients_chosen = (request.POST.getlist('ingredients_check[]'))  # pobieranie od usera
	# 	# print(ingredients_chosen)
	# 	for ingredient_chosen in ingredients_chosen:
	# 		# print(ingredient_chosen)
	# 		p = PantryIngredient.objects.get(pk=ingredient_chosen)
	# 		print(p)
	# 	base_url = reverse('core:pantry-check')
	# 	query_list = urlencode({'ingredients_chosen': ingredients_chosen})
	# 	url = '{}?{}'.format(base_url, query_list)
	# 	return redirect(url)

	ingredients_chosen = (request.GET.getlist('ingredients_check[]'))  # pobieranie od usera

	if ingredients_chosen:
		array = []
		for ingredient_chosen in ingredients_chosen:
			p = PantryIngredient.objects.get(pk=ingredient_chosen)
			array.append(p)
		print(array)
		return render(
			request,
			'core/pantry_check.html',
			context={
				'ingredients': ingredients,
				'pantry_ingredients': array,
			}
		)

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
