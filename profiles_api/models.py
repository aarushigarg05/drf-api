from re import M
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


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
    
class ProfileFeedItem(models.Model):
    # this model will allow users to store status updates in system
    # whenever a new update is made, it will make a new profile feed item and associate it with user that created it
    # we will use foreign key to associate model with model
    # integrity is maintained, never create a profile feed item for user that doesn't exist
    user_profile =models.ForeignKey(
        # we want to link it with userprofile model but we will link it through settings.py because we're passing it
        # here in a variable.. so if we change model in settings.py we don't need to manually update it here
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text =models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)
    # every time we create a new feed item, automatically add date time to item
    def __str__(self):
        # return model as string
        return self.status_text
