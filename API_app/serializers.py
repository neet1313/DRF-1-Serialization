from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=40)
