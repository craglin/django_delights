from django.db import models

# Create your models here.
class Ingredient(models.Model):
    quantity = models.IntegerField()
    price = models.IntegerField()

class MenuItem(models.Model):
    price = models.IntegerField()

class RecipeRequirement(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Purchase:
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.IntegerField()