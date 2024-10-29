from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):

    USER_TYPE = [
        ('creator', 'Recipe Creator'),
        ('viewer', 'Viewer')
    ]

    user_type = models.CharField(choices=USER_TYPE, null=True, max_length=100)
    profile_pic = models.ImageField(upload_to='Media/Profile_Pic', null=True)

    def __str__(self) -> str:
        return f"{self.username}--{self.user_type}"
    

class RecipeCreatorModel(models.Model):

    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='RecipeCreator')

    def __str__(self):
        return f"{self.user.username}"

class RecipeViewerModel(models.Model):

    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='RecipeViewer')
    
    def __str__(self):
        return f"{self.user.username}"
