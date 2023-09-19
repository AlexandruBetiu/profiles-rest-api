from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import serializers, models, permissions

# Create your views here.


class HelloApiView(APIView):

    serializer_class =  serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of features"""
        an_apiview = [
            'uses HTTP requests methods as functions (get, post, put, patch,delete)',
            'is similar to a traditional django view',
            'gives more control over the application logic',
            'is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apivew':an_apiview})
    
    def post(self,request):
        '''create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valide():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}, this is the api."
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        """update the whole obj"""
        return Response({"method":"PUT"})
    
    def patch(self,request,pk=None):
        """update only provided fileld provided in the request, of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        '''delete the obj'''
        return Response({'method':"DELETE"})


class HelloViewSet(viewsets.ViewSet):
    '''veiw for a typical api'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses functions like:list, create, retrieve, update, partial_update, delete)',
            'automatically makes(maps) the urls for you',
            'better functionaliity for less code'
        ]
        return Response({'message':"Hello!",'a_viewset':a_viewset})
    
    def create(self, request):
        '''create a new hello message'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        ''''retrieve the hello, get an obj by id'''
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        '''handle updating the whole obj(put)'''
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        '''patch'''
        return Response({'http_method':"PATCH"})
    
    def destroy(self, request, pk=None):
        '''destroy obj by pk'''
        return Response({'http_method':"DELETE"})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =( TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)