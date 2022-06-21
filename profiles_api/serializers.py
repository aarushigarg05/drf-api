from rest_framework import serializers

class HelloSerial(serializers.Serializer):
    # serializes a name field for testing our api views
    name=serializers.CharField(max_length=10)