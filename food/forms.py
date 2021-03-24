from django import forms  
from food.models import Food  

class FoodForm(forms.ModelForm):  
    class Meta:  
        model = Food  
        fields = "__all__"  