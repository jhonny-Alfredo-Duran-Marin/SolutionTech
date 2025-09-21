from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    celular = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    empresa = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.user.username
