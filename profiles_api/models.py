from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Creaza un nou user profile"""
        if not email:
            raise ValueError('Baga un email coaie')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default= False)

    objects = UserProfileManager()

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
    