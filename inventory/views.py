from distutils.log import Log
from re import L
from django.shortcuts import render
from django.shortcuts import redirect

from django.db.models import Sum, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementForm

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context



class IngredientsView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredients_list.html'


class NewIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/add_ingredient.html'

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    template_name = 'inventory/update_ingredient.html'
    model = Ingredient
    form_class = IngredientForm

class MenuView(LoginRequiredMixin, ListView):
    template_name = 'inventory/menu_list.html'
    model = MenuItem

class NewMenuItemView(LoginRequiredMixin, CreateView):
    template_name = 'inventory/add_menu_item.html'
    model = MenuItem
    form_class = MenuItemForm

class NewRecipeRequirementView(LoginRequiredMixin, CreateView):
    template_name = "inventory/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeRequirementForm
'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all()]
        context["ingredients"] = [X for X in Ingredient.objects.all()]
        

        
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        ingredient_id = request.POST["ingredient"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        ingredient = Ingredient.objects.get(pk=ingredient_id)
        recipe_requirement = RecipeRequirement(menu_item=menu_item, ingredient=ingredient)

     

        recipe_requirement.save()
        return redirect("/menu")
    
    '''

class PurchasesView(LoginRequiredMixin, ListView):
    template_name = 'inventory/purchase_list.html'
    model = Purchase



class NewPurchaseView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")


class ReportView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/reports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases'] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0

        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * \
                    recipe_requirement.quantity
        
        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context


def log_out(request):
    logout(request)
    return redirect("/")






