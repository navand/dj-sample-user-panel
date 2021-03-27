from django import forms  
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from .models import Food

import logging

class FoodForm(forms.ModelForm):  
    class Meta:  
        model = Food  
        fields = "__all__"  

class FoodAdmin(admin.ModelAdmin):  
    form = FoodForm
    list_display = ('name', 'email', 'favoriteFood')
    readonly_fields = ['name', 'email', 'telephone', 'profilePicture', 'dateOfBirth', 'favoriteFood']
        
    def save_model(self, request, obj, form, change):
        logging.info(obj.user.first_name)
        if obj.user == request.user or request.user.is_superuser:
            try:
                obj.name = obj.user.first_name + " " + obj.user.last_name
                super().save_model(request, obj, form, change)
            except:
                pass

admin.site.register(Food, FoodAdmin)
