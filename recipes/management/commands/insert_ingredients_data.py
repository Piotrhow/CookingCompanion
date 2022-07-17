from django.core.management.base import BaseCommand
from recipes.models import Ingredient,IngredientCategory, IngredientUnit

def populate_ingredientscategory():
	IngredientCategory.objects.create(name="Vegetables")
	IngredientCategory.objects.create(name="Fruits")
	IngredientCategory.objects.create(name="Dairy & Eggs")
	IngredientCategory.objects.create(name="Meat & Poultry")
	IngredientCategory.objects.create(name="Lactose-free & Meat substitutes")
	IngredientCategory.objects.create(name="Fish")
	IngredientCategory.objects.create(name="Seafood & Seaweed")
	IngredientCategory.objects.create(name="Herbs, Spices & Seasoning")
	IngredientCategory.objects.create(name="Baking")
	IngredientCategory.objects.create(name="Sugar & Sweeteners")
	IngredientCategory.objects.create(name="Dessert & Sweet Snack")
	IngredientCategory.objects.create(name="Bread & Salty Snacks")
	IngredientCategory.objects.create(name="Pasta")
	IngredientCategory.objects.create(name="Nuts & Seeds")
	IngredientCategory.objects.create(name="Grains & Cereals")
	IngredientCategory.objects.create(name="Oils & Fats")
	IngredientCategory.objects.create(name="Cheeses")
	IngredientCategory.objects.create(name="Relishes, Sauces & Dips")
	IngredientCategory.objects.create(name="Dressing & Vinegars")
	IngredientCategory.objects.create(name="Sauces & Dips")
	IngredientCategory.objects.create(name="Soup & Stew")
	IngredientCategory.objects.create(name="Beverages")
	IngredientCategory.objects.create(name="Wine, Beer & Spirits")


def populate_ingredientsunit():
	IngredientUnit.objects.create(name="g")
	IngredientUnit.objects.create(name="ml")
	IngredientUnit.objects.create(name="pcs")
	IngredientUnit.objects.create(name="tbsp")
	IngredientUnit.objects.create(name="tsp")
	IngredientUnit.objects.create(name="pinch")
	IngredientUnit.objects.create(name="drop(s)")
	# Examples relevant for cooking:
	# 1 l = 10 dl = 100 cl = 1000 ml = 1 dm3 = 0.264 US gallons
	# 1 kg = 10 hg = 1000 g = 2.2 pounds

def populate_ingredients():
	# Getting instances of existing units:
	unit_g = IngredientUnit.objects.get(name="g")
	unit_ml = IngredientUnit.objects.get(name="ml")
	unit_pcs = IngredientUnit.objects.get(name="pcs")
	unit_tbsp = IngredientUnit.objects.get(name="tbsp")
	unit_tsp = IngredientUnit.objects.get(name="tsp")
	unit_pinch = IngredientUnit.objects.get(name="pinch")
	unit_drop = IngredientUnit.objects.get(name="drop(s)")
	#
	category = IngredientCategory.objects.get(name="Vegetables")
	Ingredient.objects.create(name="carrots", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="potatoes", category=category, unit=unit_g),
	Ingredient.objects.create(name="sweet potatoes", category=category, unit=unit_g),
	Ingredient.objects.create(name="cucumbers", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="onions", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="peas", category=category, unit=unit_g),
	Ingredient.objects.create(name="kidney beans", category=category, unit=unit_g),
	Ingredient.objects.create(name="garlic", category=category, unit=unit_pcs),
	#
	category = IngredientCategory.objects.get(name="Fruits")
	Ingredient.objects.create(name="apples", category=category, unit=unit_g),
	Ingredient.objects.create(name="oranges", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="kiwifruit(kiwi)", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="bananas", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="lemons", category=category, unit=unit_pcs),
	#
	category = IngredientCategory.objects.get(name="Dairy & Eggs")
	Ingredient.objects.create(name="butter", category=category, unit=unit_g),
	Ingredient.objects.create(name="yogurt", category=category, unit=unit_g),
	Ingredient.objects.create(name="greek yogurt", category=category, unit=unit_g),
	Ingredient.objects.create(name="eggs", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="milk", category=category, unit=unit_ml),
	Ingredient.objects.create(name="sour cream", category=category, unit=unit_ml),
	#
	category = IngredientCategory.objects.get(name="Meat & Poultry")
	Ingredient.objects.create(name="bacon", category=category, unit=unit_g),
	Ingredient.objects.create(name="ham", category=category, unit=unit_g),
	Ingredient.objects.create(name="sausage", category=category, unit=unit_g),
	Ingredient.objects.create(name="prosciutto", category=category, unit=unit_g),
	Ingredient.objects.create(name="beef steak", category=category, unit=unit_g),
	Ingredient.objects.create(name="chicken breast", category=category, unit=unit_g),
	Ingredient.objects.create(name="chicken wings", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="whole chicken", category=category, unit=unit_pcs),
	#
	category = IngredientCategory.objects.get(name="Lactose-free & Meat substitutes")
	Ingredient.objects.create(name="soy milk", category=category, unit=unit_ml),
	Ingredient.objects.create(name="almond milk", category=category, unit=unit_ml),
	Ingredient.objects.create(name="condensed coconut milk", category=category, unit=unit_ml),
	Ingredient.objects.create(name="tofu", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Fish")
	Ingredient.objects.create(name="salmon", category=category, unit=unit_g),
	Ingredient.objects.create(name="canned tuna", category=category, unit=unit_g),
	Ingredient.objects.create(name="tuna", category=category, unit=unit_g),
	Ingredient.objects.create(name="truot", category=category, unit=unit_g),
	Ingredient.objects.create(name="tilapia", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Seafood & Seaweed")
	Ingredient.objects.create(name="shrimps", category=category, unit=unit_g),
	Ingredient.objects.create(name="prawns", category=category, unit=unit_g),
	Ingredient.objects.create(name="oysters", category=category, unit=unit_g),
	Ingredient.objects.create(name="lobster", category=category, unit=unit_pcs),
	#
	category = IngredientCategory.objects.get(name="Herbs, Spices & Seasoning")
	Ingredient.objects.create(name="salt", category=category, unit=unit_g),
	Ingredient.objects.create(name="black pepper grounded", category=category, unit=unit_g),
	Ingredient.objects.create(name="black pepper grains", category=category, unit=unit_g),
	Ingredient.objects.create(name="red pepper flakes", category=category, unit=unit_pinch),
	Ingredient.objects.create(name="curry", category=category, unit=unit_g),
	Ingredient.objects.create(name="chilli powder", category=category, unit=unit_pinch),
	Ingredient.objects.create(name="sweet pepper", category=category, unit=unit_g),
	Ingredient.objects.create(name="basil fresh leaves", category=category, unit=unit_g),
	Ingredient.objects.create(name="basil dried", category=category, unit=unit_g),
	Ingredient.objects.create(name="oregano dried", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Baking")
	Ingredient.objects.create(name="flour", category=category, unit=unit_g),
	Ingredient.objects.create(name="cake flour", category=category, unit=unit_g),
	Ingredient.objects.create(name="almond flour", category=category, unit=unit_g),
	Ingredient.objects.create(name="whole-wheat flour", category=category, unit=unit_g),
	Ingredient.objects.create(name="baking powder", category=category, unit=unit_g),
	Ingredient.objects.create(name="baking soda", category=category, unit=unit_g),
	Ingredient.objects.create(name="yeast", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Sugar & Sweeteners")
	Ingredient.objects.create(name="sugar", category=category, unit=unit_g),
	Ingredient.objects.create(name="brown sugar", category=category, unit=unit_g),
	Ingredient.objects.create(name="honey", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Sugar & Sweeteners")
	Ingredient.objects.create(name="cocoa", category=category, unit=unit_g),
	Ingredient.objects.create(name="vanilla", category=category, unit=unit_g),
	Ingredient.objects.create(name="vanilla extract", category=category, unit=unit_tsp),
	Ingredient.objects.create(name="chocolate", category=category, unit=unit_g),
	Ingredient.objects.create(name="white chocolate", category=category, unit=unit_g),
	Ingredient.objects.create(name="dark chocolate", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Bread & Salty Snacks")
	Ingredient.objects.create(name="bread", category=category, unit=unit_pcs),
	Ingredient.objects.create(name="bread crumbs", category=category, unit=unit_g),
	Ingredient.objects.create(name="baguette", category=category, unit=unit_g),
	Ingredient.objects.create(name="crackers", category=category, unit=unit_g),
	Ingredient.objects.create(name="pita", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Pasta")
	Ingredient.objects.create(name="penne", category=category, unit=unit_g),
	Ingredient.objects.create(name="spaghetti", category=category, unit=unit_g),
	Ingredient.objects.create(name="noodle", category=category, unit=unit_g),
	Ingredient.objects.create(name="fusilli", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Nuts & Seeds")
	Ingredient.objects.create(name="almonds", category=category, unit=unit_g),
	Ingredient.objects.create(name="walnuts", category=category, unit=unit_g),
	Ingredient.objects.create(name="pecan nuts", category=category, unit=unit_g),
	Ingredient.objects.create(name="sesame seeds", category=category, unit=unit_g),
	Ingredient.objects.create(name="chia seeds", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Grains & Cereals")
	Ingredient.objects.create(name="rice", category=category, unit=unit_g),
	Ingredient.objects.create(name="brown rice", category=category, unit=unit_g),
	Ingredient.objects.create(name="sushi rice", category=category, unit=unit_g),
	Ingredient.objects.create(name="couscous", category=category, unit=unit_g),
	Ingredient.objects.create(name="quinoa", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Oils & Fats")
	Ingredient.objects.create(name="olive oil", category=category, unit=unit_g),
	Ingredient.objects.create(name="coconut oil", category=category, unit=unit_g),
	Ingredient.objects.create(name="sesame oil", category=category, unit=unit_g),
	Ingredient.objects.create(name="sunflower oil", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Cheeses")
	Ingredient.objects.create(name="parmesan", category=category, unit=unit_g),
	Ingredient.objects.create(name="parmigiano-reggiano cheese", category=category, unit=unit_g),
	Ingredient.objects.create(name="cheddar", category=category, unit=unit_g),
	Ingredient.objects.create(name="mozzarella", category=category, unit=unit_g),
	Ingredient.objects.create(name="ricotta", category=category, unit=unit_g),
	Ingredient.objects.create(name="mascarpone", category=category, unit=unit_g),
	Ingredient.objects.create(name="feta cheese", category=category, unit=unit_g),
	Ingredient.objects.create(name="goat cheese", category=category, unit=unit_g),
	#
	category = IngredientCategory.objects.get(name="Relishes, Sauces & Dips")
	Ingredient.objects.create(name="soy sauce", category=category, unit=unit_tbsp),
	Ingredient.objects.create(name="dijon mustard", category=category, unit=unit_g),
	Ingredient.objects.create(name="ketchup", category=category, unit=unit_g),
	Ingredient.objects.create(name="mayonnaise", category=category, unit=unit_g),
	Ingredient.objects.create(name="worcestershire sauce", category=category, unit=unit_ml),
	Ingredient.objects.create(name="hot sauce", category=category, unit=unit_ml),
	Ingredient.objects.create(name="bbq sauce", category=category, unit=unit_ml),
	Ingredient.objects.create(name="green olives", category=category, unit=unit_g),
	Ingredient.objects.create(name="black olives", category=category, unit=unit_g),
	Ingredient.objects.create(name="dried tomatoes", category=category, unit=unit_g),
	Ingredient.objects.create(name="tahini", category=category, unit=unit_g),
	Ingredient.objects.create(name="marinara sauce", category=category, unit=unit_g),
	Ingredient.objects.create(name="can tomatoes", category=category, unit=unit_g),
	Ingredient.objects.create(name="tomato sauce", category=category, unit=unit_g),
	Ingredient.objects.create(name="tomato paste", category=category, unit=unit_tbsp),
	#
	category = IngredientCategory.objects.get(name="Dressing & Vinegars")
	Ingredient.objects.create(name="apple cider vinegar", category=category, unit=unit_ml),
	Ingredient.objects.create(name="red wine vinegar", category=category, unit=unit_ml),
	Ingredient.objects.create(name="rice wine vinegar", category=category, unit=unit_ml),
	Ingredient.objects.create(name="white wine vinegar", category=category, unit=unit_ml),
	Ingredient.objects.create(name="balsamic vinegar", category=category, unit=unit_ml),
	Ingredient.objects.create(name="sherry vinegar", category=category, unit=unit_ml),
	Ingredient.objects.create(name="vinegar", category=category, unit=unit_ml),
	#
	category = IngredientCategory.objects.get(name="Soup & Stew")
	Ingredient.objects.create(name="chicken broth", category=category, unit=unit_ml),
	Ingredient.objects.create(name="vegetable broth", category=category, unit=unit_ml),
	Ingredient.objects.create(name="bulion cube", category=category, unit=unit_g),

	category = IngredientCategory.objects.get(name="Beverages")
	Ingredient.objects.create(name="water", category=category, unit=unit_ml),
	Ingredient.objects.create(name="club soda", category=category, unit=unit_ml),
	Ingredient.objects.create(name="coffee", category=category, unit=unit_ml),
	Ingredient.objects.create(name="orange juice", category=category, unit=unit_ml),

	category = IngredientCategory.objects.get(name="Wine, Beer & Spirits")
	Ingredient.objects.create(name="red wine wry", category=category, unit=unit_ml),
	Ingredient.objects.create(name="red wine sweet", category=category, unit=unit_ml),
	Ingredient.objects.create(name="white wine dry", category=category, unit=unit_ml),
	Ingredient.objects.create(name="bourbon", category=category, unit=unit_ml),
	Ingredient.objects.create(name="cider", category=category, unit=unit_ml),
	Ingredient.objects.create(name="rum", category=category, unit=unit_ml),


class Command(BaseCommand):
	help = 'Creates ingredients along with its units and categories'

	def handle(self, *args, **kwargs):
		populate_ingredientsunit()
		populate_ingredientscategory()
		populate_ingredients()