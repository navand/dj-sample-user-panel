from django.db import models
from django.conf import settings

class Food(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, unique=False)
    name = models.CharField(max_length=100, null=True)  
    email = models.EmailField(null=True)  
    telephone = models.CharField(max_length=15, null=True)
    profilePicture = models.ImageField(upload_to="uploads", default='e.png')
    dateOfBirth = models.DateField(null=True)
    favoriteFood = models.CharField(max_length=100, null=True)

    class Meta:  
        db_table = "food"
        verbose_name = "Food form"

    def __str__(self):
        return ''