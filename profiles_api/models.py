from re import M
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    # manager for user profile

    def create_user(self,email,name,password=None):
        # create a new user, password is set to None, it means we can't create a user until a password is set
        # so if we don't specify a password then it will default to none
        if not email:
            raise ValueError('Enter a valid email address')
        
        email=self.normalize_email(email)
        user=self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email,name,password):
        # we don't pass none here because we want all superusers to have a password
        user=self.create_user(email,name,password)

        user.is_superuser=True
        # built in function of PermissionMixIn
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # database model for users in system
    email=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        return self.name
    def short_name(self):
        return self.name
    
    # isse email display hogi at admin page
    def __str__(self):
        return self.email
