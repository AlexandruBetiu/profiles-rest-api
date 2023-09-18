from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

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


