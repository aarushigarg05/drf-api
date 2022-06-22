from ast import Is
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import models
from profiles_api import permissions


class HelloView(APIView):
    serializer_class = serializers.HelloSerial

    def get(self, request, format=None):
        # returns a list of API view features
        an_apiview=[
            'similar to django view',
            'mapped manually to urls',
        ]

        return Response({'message': 'Hello','an_apiview':an_apiview})

    def post(self, request):
        # creates a message with name passed in serializer
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            # f string functionality to insert string
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        # put is used to update the objects, and put is done to a specific url primary key,
        # but we default it to none in case we don't want to support it in our api views.
        # woth pk we get id of object we need to update
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        # used to handle partial updates of objects 
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk=None):
        # used to delete objects
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerial
    def list(self, request):
        # same as get
        a_viewset=[
            'similar to django view',
            'mapped manually to urls',
        ]

        return Response({'message': 'Hello','a_viewset': a_viewset})

        
    def create(self,request):
        # same as post
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            # f string functionality to insert string
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        # retreives a particular object by it's id
        return Response({'message':'Get'})
    
    def update(self, request, pk=None):
        # same as put
        return Response({'message':'Update'})
    
    def partial_update(self, request, pk=None):
        # same as patch
        return Response({'message':'Patch'})
    
    def destroy(self, request, pk=None):
        # same as delete
        return Response({'message':'Delete'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    # we provide a queryset to modelviewset so it knows which objects of db it should manage
    # handles creating and update profiles 
    serializer_class = serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    # drf automatically knows that we need basic function like create, update, etc when we assign 
    # serializer and query set and defines these functions for us
    authentication_class = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends =(filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    # we could have directly added obtainauthtoken in urls but it doesn't enable itself in browsable django site.
    # so we enable it here by adding renderer_classes which are not added to it by default
    # This class UserLoginApiView handles creating user authentication tokens
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    # handles creating, reading and updating profile feed item
    authentication_classes=(TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    # user_profile is read_only and we need to set it on basis of authenticated user only
    # so we add perform_create, it will override the behaviour of creating objects through model viewset
    # when reuqest gets made, it gets passed to serializer and validated
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
        # user should be authenticated or it's access is read only
    )

    def perform_create(self,serializer):
        # sets user profile to logged in user
        # hhtp post calls this function
        serializer.save(user_profile=self.request.user)
        # when a new object is created and passes serializer that is used to create object
        # this saves contents to an object in db
        # here we call save serializer and pass additional keyword for user_profile 
        # request is passes to all viewsets every time a reuqest is made and contains all details about request being made to viewset
        # if user is authenticated, request will have a user and user field gets added
        # if user is not authenticated, then anonymous user will be added






        
