from django.db import models
from django.conf import settings

class Food(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, unique=False)
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    telephone = models.CharField(max_length=15)
    profilePicture = models.CharField(max_length=15)
    dateOfBirth = models.DateField()
    favoriteFood = models.CharField(max_length=100)

    class Meta:  
        db_table = "food"

    def __str__(self):
        return self.name + self.favoriteFood