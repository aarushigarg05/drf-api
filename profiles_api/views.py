from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


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




        
