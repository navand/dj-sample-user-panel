from django.shortcuts import render, redirect  
from food.forms import FoodForm  
from food.models import Food  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = FoodForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = FoodForm()  
    return render(request,'index.html',{'form':form})  
def index(request):  
    foods = Food.objects.all()  
    return render(request,"show.html",{'foods':foods})  
def edit(request, id):  
    food = Food.objects.get(id=id)  
    return render(request,'edit.html', {'food':food})  
def update(request, id):  
    food = Food.objects.get(id=id)  
    form = FoodForm(request.POST, instance = food)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'food': food})  
def destroy(request, id):  
    food = Food.objects.get(id=id)  
    food.delete()  
    return redirect("/show")  