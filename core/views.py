from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views
from django.db import IntegrityError

from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import Pantry, PantryIngredient
from recipes.models import Ingredient, IngredientCategory

EMPTY_MSG = 'It looks like you don\'t have anything yet.'
DUPLICATE_MSG = 'It looks like you already have that item. Try updating the existing amount instead.'
WRONG_NAME_MSG = 'Something\'s wrong. Try again and make sure you don\'t make any typos.'


# Create your views here.
def pantry_detail(request):

	if request.user.is_authenticated:
		id = request.user.id
		p = get_object_or_404(Pantry, user_id=id)
	else:
		return redirect('/login')

	pantry_id = p.id
	pi_all = PantryIngredient.objects.filter(pantry_id=pantry_id)
	categories_all = IngredientCategory.objects.all()

	return render(
		request,
		'core/pantry_detail.html',
		context={
			'pantry_ingredients': pi_all,
			'empty_msg': EMPTY_MSG,
			'categories_all': categories_all,
		}
	)


# CREATE PANTRY INGREDIENT
def pantryingredient_create(request):

	id = request.user.id
	p = get_object_or_404(Pantry, user_id=id)
	pantry_id = p.id
	pi_all = PantryIngredient.objects.filter(pantry_id=p.id)
	ingredients = Ingredient.objects.all()
	categories_all = IngredientCategory.objects.all()

	# flag = 0

	if request.method == "POST":

		ingredient_name = (request.POST.get('ingredient_name')) #pobieranie od usera
		quantity = request.POST.get('quantity') #pobieranie od usera

		if ingredient_name and quantity:
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
			except AttributeError:
				flag = 2
			res = redirect('core:create')
			res.set_cookie("flag", flag)
			return res

	else:

		ingredient_category = (request.GET.get('ingredient_category')) #pobieranie od usera

		flag = request.COOKIES.get("flag", 0)

		if flag:
			flag = int(flag)

		if ingredient_category:
			ingredients = Ingredient.objects.filter(category__name=ingredient_category)


		res = render(
			request,
			'core/pantryingredient_form.html',
			context={
				'pantry_ingredients': pi_all, #jeżeli nie będzie tego - to nie pokaże listy
				'categories_all': categories_all, #jeżeli nie będzie tego - to nie pokaże listy
				'empty_msg': EMPTY_MSG,
				'duplicate_msg': DUPLICATE_MSG,
				'wrong_name_msg': WRONG_NAME_MSG,
				'flag': flag,
				'ingredients': ingredients,

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
	# id = request.user.id
	# p = get_object_or_404(Pantry, user_id=id)
	# pi_all = PantryIngredient.objects.filter(pantry_id=p.id)

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
			# 'pantry_ingredients': pi_all, #jeżeli nie będzie tego - to nie pokaże listy
			'ingredient': ingredient,
			'quantity_old': quantity_old,
		}
	)

