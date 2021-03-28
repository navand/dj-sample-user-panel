from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Food
from .forms import FoodForm

@login_required(login_url="/")
@permission_required('food.view_food', login_url="/")
def all_foods(request):
    foods = Food.objects.filter(user=request.user)
    context = {
        'foods': foods
    }
    return render(request, 'food/index.html', context)

@login_required(login_url="/")
@permission_required('food.change_food', login_url="/")
def edit_foods(request, id=None):
    try:
        one_food = Food.objects.get(id=id)
    except Food.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Food notfound")
        return redirect('food')

    if(one_food.user.id != request.user.id):
        messages.add_message(request, messages.ERROR, "You haven't access to this food")
        return redirect('food')

    form = FoodForm(request.POST or None, request.FILES or None, instance=one_food)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, "Your food has been updated")
        return redirect('food')

    context = {
        'form': form,
    }
    return render(request, 'food/edit.html', context)

@login_required(login_url="/")
@permission_required('food.view_food', login_url="/")
def one_food(request, id=None):
    try:
        food = Food.objects.get(id=id)
    except Food.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Food notfound")
        return redirect('food')

    if(food.user != request.user):
        messages.add_message(request, messages.ERROR, "You haven't access to this food")
        return redirect('food')

    context = {
        'food': food
    }
    return render(request, 'food/view.html', context)
