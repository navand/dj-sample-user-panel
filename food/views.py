from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Food
from .forms import FoodForm

@login_required(login_url="/")
def all_foods(request):
    foods = Food.objects.filter(user=request.user)
    context = {
        'foods': foods
    }
    return render(request, 'food/index.html', context)

@login_required(login_url="/")
# @permission_required('food.can_edit')
def edit_foods(request, id=None):
    one_food = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, request.FILES or None, instance=one_food)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} has been added")
        return redirect('food')

    context = {
        'form': form,
    }
    return render(request, 'food/edit.html', context)


def one_food(request, id=None):
    food = Food.objects.get(id=id)
    context = {
        'food': food
    }
    return render(request, 'food/viewFood.html', context)

def home_view(request):
    context = dict()
    return render(request, 'food/home.html', context)
