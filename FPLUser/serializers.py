from rest_framework import serializers
from .models import FPLUser

class FPLUser_serializer(serializers.ModelSerializer):
    class Meta:
        model = FPLUser
        fields = ("id","username","email","balance","points","players","startingXI")