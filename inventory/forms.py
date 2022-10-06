from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
    
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'


def get_choice(lst):
        choices = []
        for i in range(len(lst)):
            temp_lst = lst[i][0]
            temp_tuple = (temp_lst, temp_lst)
            choices.append(temp_tuple)
        
        return choices
    
   
class RecipeRequirementForm(forms.ModelForm):
    '''
   def __init__(self, *args, **kwargs):
        
        super(RecipeRequirementForm, self).__init__(*args, **kwargs)
       
        titles = get_choice([ (o.title, o) for o in MenuItem.objects.all()])
        self.fields['menu_item'] = forms.ChoiceField(choices=titles)
        
        names = get_choice([ (o.name, o) for o in Ingredient.objects.all()])
        self.fields['ingredient'] = forms.ChoiceField(choices=names)'''

    class Meta:
        model = RecipeRequirement
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


