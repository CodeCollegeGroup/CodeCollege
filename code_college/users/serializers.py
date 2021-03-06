from rest_framework import serializers
from .models import OrdinaryUser


class OrdinaryUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdinaryUser
        fields = [
            'id',
            'username',
        ]
