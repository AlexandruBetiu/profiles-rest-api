from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default= False)

    objects = UserPrifileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name... what did you think it does? """
        return self.name
    
    def __str__(self):
        """return string representation of the class(user aour case here)"""
        return self.email
    