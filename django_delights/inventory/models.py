from django.db import models
from django.utils import timezone, dateformat

# Create your models here.
class Ingredient(models.Model):
    
    UNIT_CHOICES = [
        ('each', 'Each'),
        ('dz', 'Dozen'),
        ('tsp', 'Teaspoon'),
        ('tbsp', 'Tablespoon'),
        ('gram', 'Gram'),
        ('oz', 'Ounce'),
        ('lb', 'Pound'),
    ]

    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(
        max_length=50,
        choices= UNIT_CHOICES,
        default='each')

    def __str__(self) -> str:
        return f"{self.quantity} of {self.name}"

class MenuItem(models.Model):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name} at ${self.price}"

class RecipeRequirement(models.Model):
    items = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)

class Purchase(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    f_time = dateformat.format(time, 'Y/m/d')

    def __str__(self):
        return f"{self.item} on {self.f_time}"
    