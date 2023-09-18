from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for our profiles api'''
    name = serializers.CharField(max_length=100)