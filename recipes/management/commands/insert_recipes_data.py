from django.core.management.base import BaseCommand
from recipes.models import Recipe, RecipeIngredient, Ingredient


def populate_recipes():
	Recipe.objects.create(
		name="Margherita Pizza",
		picture="recipe_images/pizza.jpg",
		description='''
		<b>Prepare Pizza Dough: </b>
		<br>
		In a medium bowl, whisk together the all-purpose flour, sugar, yeast and salt. 
		Add the warm water and olive oil, and stir the mixture with a wooden spoon until the dough just begins 
		to come together. 
		It will seem shaggy and dry, but don’t worry.
		<br>
		Scrape the dough onto a well-floured counter top and knead the dough for three minutes. 
		It should quickly come together and begin to get sticky. Dust the dough with flour as needed 
		(sometimes I will have to do this 2 to 3 times, depending on humidity levels) – it should be slightly tacky, 
		but should not be sticking to your counter top.  After about 3 minutes, the dough should be smooth, slightly 
		elastic, and tacky. Lightly grease a large mixing bowl with olive oil, and place the dough into the bowl.
		<br>
		Cover the bowl with a kitchen towel (or plastic wrap) and allow the dough to rise in a warm, 
		dry area of your kitchen for 2 hours or until the dough has doubled in size. 
		Proofing Tip: If your kitchen is very cold, heat a large heatproof measuring cup of water in the microwave 
		for 2 to 3 minutes. This creates a nice warm environment. 
		Remove the cup and place the bowl with the dough in the microwave until it has risen. 
		[If you are preparing the dough in advance, see the note section for freezing instructions.]
		<br>
		<b>Preheat Oven and Pizza Steel or Stone:</b> Place the pizza steel (or stone) on the second to top rack of your oven 
		(roughly 8 inches from the broiler element), and preheat the oven and steel (or stone) to 550°F (285°C) 
		for a minumum of 1 hour. If your oven does not go up to 550°F (285°C) or you are using a delicate pizza stone, 
		I recommend heating it to a maximum of 500°F (260°C)
		<br>
		As the oven is preheating, assemble the ingredients. In a small bowl, stir together the pureed tomatoes, 
		minced garlic, extra virgin olive oil, pepper, and salt. Set aside another small bowl with the cubed mozzarella 
		cheese (pat the cheese with a paper towel to remove any excess moisture). Set aside the basil leaves and 
		grated parmigiano-reggiano cheese for easy grabbing.
		<br>
		Separate the dough into two equal-sized portions. It will deflate slightly, but that is OK. 
		Place the dough on a large plate or floured counter top, cover gently with plastic wrap, and allow the dough 
		to rest for 5 to 10 minutes.
		<br>
		<b>Assemble the Pizza:</b> Sprinkle the pizza peel (if you do not own a pizza peel, you can try using the back of 
		a half sheet pan - but it is tricky!) with a tablespoon of semolina and dusting of all-purpose flour. 
		Gently use both hands to stretch one ball of pizza dough into roughly a 10-inch circle 
		(don’t worry if its not perfectly uniform). If the dough springs back or is too elastic, 
		allow it to rest for an additional five minutes. The edges of the dough can be slightly thicker, but make sure 
		the center of the dough is thin (you should be able to see some light through it if you held it up). 
		Gently transfer the dough onto the semolina and flour dusted pizza peel or baking sheet.
		<br>
		Drizzle or brush the dough lightly (using your fingertips) with olive oil (roughly a teaspoon. 
		Using a large spoon, add roughly ½ cup of the tomato sauce onto the pizza dough, leaving a ½-inch or ¾-inch 
		border on all sides. Use the back of the spoon to spread it evenly and thinly. Sprinkle a tablespoon of 
		parmigiano-reggiano cheese onto the pizza sauce. Add half of the cubed mozzarella, distributing it evenly 
		over the entire pizza. Using your hands, tear a few large basil leaves, and sprinkle the basil over the pizza. 
		At this point, I’ll occasionally stretch the sides of the dough out a bit to make it even thinner. 
		Gently slide the pizza from the peel onto the heated baking stone. Bake for 7 to 8 minutes, or until the crust 
		is golden and the cheese is bubbling and caramelized and the edges of the pizza are golden brown. 
		Note: If you're looking for more color, finish the pizza under the low or medium broil setting, 
		but watch it carefully!
		Remove the pizza carefully from the oven with the pizza peel, transfer to a wooden cutting board or foil, 
		drizzle the top with olive oil, some grated parmigiano-reggiano cheese, and chiffonade of fresh basil. 
		Slice and serve immediately and/or prepare the second pizza.
		'''
	)
	Recipe.objects.create(
		name="Easy Three-Ingredient Tomato Soup",
		picture="recipe_images/tomato_soup.jpg",
		description='''
		Melt butter over medium heat in a Dutch oven or large saucepan.
		<br>
		Add onion wedges, water, can of tomatoes with their juices, and 1/2 teaspoon of salt. Bring to a simmer. 
		Cook, uncovered, for about 40 minutes. Stir occasionally and add additional salt as needed.
		<br>
		Blend the soup, and then season to taste. The soup doesn’t need to be ultra-smooth, some texture is a nice touch. 
		An immersion blender does make quick work of this, or you can use a blender. If you use a regular blender, 
		it is best to blend in batches and not fill the blender as much as you usually would since the soup is so hot. 
		We like to remove the center insert of the lid and cover it with a kitchen towel while blending — this helps 
		to release some of the steam and prevents the blender lid from popping off (which can be a big, hot mess).
	'''
	)
	Recipe.objects.create(
		name="Fluffy Pancakes from Scratch",
		picture="recipe_images/pancakes.jpg",
		description='''
		<b>MAKE BATTER</b>
		Whisk flour, sugar, baking powder, and the salt in a medium bowl.
		<br>
		Warm milk in the microwave or on top of the stove until lukewarm, not hot. You should be able to keep your 
		finger submerged for 10 seconds.
		<br>
		Whisk milk, egg, melted butter, and vanilla extract until combined. (By warming the milk slightly, the melted 
		butter mixes into the milk instead of turning into small lumps).
		<br>
		<b>COOK PANCAKES</b>
		Heat a large skillet (or use griddle) over medium heat. The pan is ready if when you splatter a little water 
		onto the pan surface, the water dances around the pan and eventually evaporates.		
		<br>
		Make a well in the center of the flour mixture, pour milk mixture into the well and use a fork to stir until 
		you no longer see clumps of flour. It is okay if the batter has small lumps – it is important not to over-mix 
		the batter.
		<br>
		Lightly brush skillet with melted butter (this is optional if you have a high-quality non-stick pan). 
		Use a 1/4-cup measuring cup to spoon batter onto the skillet. Gently spread the batter into a 4-inch circle.
		<br>
		When edges look dry, and bubbles start to appear and pop on the top surfaces of the pancake, turn over. 
		This takes about 2 minutes. Once flipped, cook another 1 to 2 minutes or until lightly browned and cooked in 
		the middle. Serve immediately with warm syrup, butter, and berries.
		'''
	)


def populate_recipeingredients():
	# Getting ingredients from existing data_base
	butter = Ingredient.objects.get(name="butter")
	onions = Ingredient.objects.get(name="onions")
	can_tomatoes = Ingredient.objects.get(name="can tomatoes")
	water = Ingredient.objects.get(name="water")
	salt = Ingredient.objects.get(name="salt")
	flour = Ingredient.objects.get(name="flour")
	sugar = Ingredient.objects.get(name="sugar")
	yeast = Ingredient.objects.get(name="yeast")
	olive_oil = Ingredient.objects.get(name="olive oil")
	garlic = Ingredient.objects.get(name="garlic")
	mozzarella = Ingredient.objects.get(name="mozzarella")
	parmigiano_reggiano_cheese = Ingredient.objects.get(name="parmigiano-reggiano cheese")
	baking_powder = Ingredient.objects.get(name="baking powder")
	milk = Ingredient.objects.get(name="milk")
	eggs = Ingredient.objects.get(name="eggs")
	vanilla_extract = Ingredient.objects.get(name="vanilla extract")

	recipe = Recipe.objects.get(name="Margherita Pizza")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=flour, quantity="300")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=sugar, quantity="5")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=yeast, quantity="15")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=salt, quantity="5")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=water, quantity="450")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=olive_oil, quantity="50")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=can_tomatoes, quantity="1")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=garlic, quantity="15")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=mozzarella, quantity="150")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=parmigiano_reggiano_cheese, quantity="300")

	#
	recipe = Recipe.objects.get(name="Easy Three-Ingredient Tomato Soup")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=butter, quantity="15")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=onions, quantity="1")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=can_tomatoes, quantity="1")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=water, quantity="300")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=salt, quantity="5")
	#
	recipe = Recipe.objects.get(name="Fluffy Pancakes from Scratch")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=flour, quantity="200")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=sugar, quantity="20")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=baking_powder, quantity="10")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=salt, quantity="5")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=milk, quantity="295")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=eggs, quantity="1")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=butter, quantity="40")
	RecipeIngredient.objects.create(recipe=recipe, ingredient=vanilla_extract, quantity="1")


class Command(BaseCommand):
	help = 'Creates ingredients along with its units and categories'

	def handle(self, *args, **kwargs):
		populate_recipes()
		populate_recipeingredients()