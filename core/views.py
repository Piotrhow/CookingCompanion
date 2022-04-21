from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django import views

from django.views.generic import CreateView, DetailView, ListView, TemplateView

from core.models import Ingredient, Pantry, PantryIngredient
# from accounts.models import User

# Create your views here.
def pantry_detail(request):

	if request.user.is_authenticated:
		id = request.user.id
		p = get_object_or_404(Pantry, user_id=id)
		print(f"Username --> {request.user.username}")
	else:
		return redirect('/login')

	id_of_pantry = p.id
	pi = PantryIngredient.objects.filter(pantry_id=id_of_pantry)

	empty_msg = 'It looks like you don\'t have anything yet.'

	return render(
		request,
		'core/pantry_detail.html',
		context={
			'pantry': p,
			'pantry_ingredients': pi,
			'id': id,
			'empty_msg': empty_msg
		}
	)

# CREATE PANTRY INGREDIENT