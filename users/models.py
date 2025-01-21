from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):  
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'