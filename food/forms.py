from django import forms  
from food.models import Food  

class DateInput(forms.DateInput):
    input_type = 'date'

class FoodForm(forms.ModelForm):  
    class Meta:  
        model = Food  
        # fields = "__all__"  
        exclude = ('user',)

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={             
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={             
                "class": "form-control"
            }
        ))
    telephone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$', 
        error_messages = {"invalid":"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."},
        widget=forms.TextInput(
            attrs={             
                "class": "form-control"
            }
        ))
    profilePicture = forms.ImageField(
        label="Profile picture",
        widget=forms.FileInput(
            attrs={             
                "class": "form-control"
            }
        ))
    dateOfBirth = forms.CharField(
        label="Date of birth",
        widget=DateInput(
            attrs={             
                "class": "form-control"
            }
        ))
    favoriteFood = forms.CharField(
        label="Favorite food",
        widget=forms.TextInput(
            attrs={             
                "class": "form-control"
            }
        ))
