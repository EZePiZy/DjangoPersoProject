from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name', 'quantity', 'unit', 'price_per_unit')

@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):
    model = MenuItem
    list_display = ('title', 'price')

@admin.register(RecipeRequirement)
class RecipeRequirement(admin.ModelAdmin):
    model = RecipeRequirement
    list_display = ('get_menu_item','get_ingredient', 'quantity')

    def get_menu_item(self, obj):
        return obj.menu_item.title
    
    def get_ingredient(self, obj):
        return obj.ingredient.name
    
    get_menu_item.admin_order_field = 'title'
    get_ingredient.admin_order_fiels = 'name'

@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    model = Purchase
    list_display = ('get_menu_item', 'timestamp')

    def get_menu_item(self, obj):
        return obj.menu_item.title
    
