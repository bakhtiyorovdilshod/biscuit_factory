from django.contrib import admin

from apps.recipe.models import ManufacturedProductRecipe
from apps.recipe.models.biscuit_recipe import BiscuitRecipe

admin.site.register(BiscuitRecipe)
admin.site.register(ManufacturedProductRecipe)





