from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views

from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import Ingredient, Pantry, PantryIngredient

EMPTY_MSG = 'It looks like you don\'t have anything yet.'

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

	return render(
		request,
		'core/pantry_detail.html',
		context={
			'pantry': p,
			'pantry_ingredients': pi,
			'id': id,
			'empty_msg': EMPTY_MSG
		}
	)

# CREATE PANTRY INGREDIENT
def pantryingredient_create(request):
	ingredient_id = request.POST.get('ingredient_id')
	quantity = request.POST.get('quantity')
	id = request.user.id
	p = get_object_or_404(Pantry, user_id=id)
	pantry_id = p.id
	pi = PantryIngredient.objects.filter(pantry_id=pantry_id)


	if ingredient_id and quantity:
		PantryIngredient.objects.create(
			pantry_id=pantry_id,
			quantity=quantity,
			ingredient_id=ingredient_id,
		)
		return redirect('core:pantry-detail')

	return render(
        request,
        'core/pantryingredient_form.html',
		context={
			'pantry': p,
			'pantry_ingredients': pi,
			'id': id,
			'empty_msg': EMPTY_MSG
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

