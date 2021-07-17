from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from foods.models import Menu
# Create your views here.
def index(request):
  context = dict()
  today = datetime.today().date()
  menus = Menu.objects.all()
  
  return render(request, 'foods/index.html',{
    "today": today,
    "menus": menus
    })

def food_detail(request,pk):
  context = dict()
  menu = Menu.objects.get(id=pk)
  context["menu"] = menu
  return render(request,'foods/detail.html',context=context)
  