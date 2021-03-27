from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_foods, name='food'),
    path('editFood/<int:id>', views.edit_foods, name='editFood'),
    path('viewFood/<int:id>', views.one_food, name='oneFood'),
]
