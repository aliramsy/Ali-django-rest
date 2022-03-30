from rest_framework import serializers
from .models import Student


class StudentSer(serializers.ModelSerializer):
    class Meta():
        model= Student
        fields=("name", "age")
        


