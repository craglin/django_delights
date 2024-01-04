from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def ingredients_list(request):
    ingredients = Ingredient.objects.all()
    return HttpResponse()

def ingredients_delete(request, ingredient_ID):
    ingredient = Ingredient.objects.get(pk=ingredient_ID)
    pass

def menuitems_list(request):
    pass

def menuitems_delete(request, menuitem_ID):
    pass

def purchases_list(request):
    pass

def profit(request):
    pass

