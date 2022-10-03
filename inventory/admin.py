from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'price_per_unit')

@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(RecipeRequirement)
class RecipeRequirement(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient', 'quantity')

    
    

@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    list_display = ('menu_item', 'timestamp')
