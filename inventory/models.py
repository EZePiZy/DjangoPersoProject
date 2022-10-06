from django.db import models


class MenuItem(models.Model):
 
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def __str__(self):
        return f"title={self.title}; price={self.price}"


    class Meta: 
        ordering=['price']


class Ingredient(models.Model):
  
    LBS = "lbs"
    TBSP = "tbsp"
    GRAMS = 'grams'
    KILO = 'kilo'
    EGG = 'Egg'
    UNIT_CHOICE = [
        (LBS, 'Pound'),
        (TBSP, 'Ounce'),
        (GRAMS, 'grams'),
        (KILO, 'kg'),
        (EGG, 'egg')
    ]
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0.00)
    unit = models.CharField(max_length=15, choices=UNIT_CHOICE, default=LBS)
    price_per_unit = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"
    

    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """

    class Meta:
        ordering = ['unit']

class RecipeRequirement(models.Model):
 
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


    def __str__(self):
        return f"""
        menu_item={self.menu_item.title}; 
        ingredient={self.ingredient.name}; 
        qty={self.quantity}"""
    
    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        return self.quantity <= self.ingredient.quantity

class Purchase(models.Model):
 
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"
