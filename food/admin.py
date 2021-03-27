from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from .models import Food
from .forms import FoodForm

import logging

class FoodAdmin(admin.ModelAdmin):  
    form = FoodForm
    # list_display = ('name', 'email', 'favoriteFood')
    # readonly_fields = ['name', 'email', 'telephone', 'profilePicture', 'dateOfBirth', 'favoriteFood']
        
    def save_model(self, request, obj, form, change):
        logging.info("I'm here")
        if obj.user == request.user or request.user.is_superuser:
            try:
                super().save_model(request, obj, form, change)
            except:
                pass

admin.site.register(Food, FoodAdmin)
