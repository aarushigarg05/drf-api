from rest_framework import serializers
from profiles_api import models

class HelloSerial(serializers.Serializer):
    # serializes a name field for testing our api views
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    # serializes a user profile object

    class Meta:
        model=models.UserProfile
        fields=('id','name', 'email','password')
        # fields we want to use (in a tuple)
        # exception to password because we want to use it while making new users only
        # we want to make password field write only
        extra_kwargs={
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}
            }
        }
        # over write the create function as by default the model serializer allows us to create simple objects in _db
        # it uses default create function. we make create user function instead of create function. we do this so that 
        # password is created as hash and not as clear text as it would do in default

    def create(self,validated_data):
        # whenever an object is created, our serializer will validate it and then will call create function and will pass the validated data to create and return user
            # creates and returns a new user
            user=models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password'],
            )
            user.save()
            return user
# create_user is a function defined in userprofilemanager in models.py
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    # serializes profile feed items
    class Meta:
        model=models.ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        # id is by default read only and same for created_on
        # user_profile needs to be based on user authenticated and we don't want users to create anew user profile feed item and assign it to other user 
        extra_kwargs={
            'user_profile':{'read_only': True}
        }

