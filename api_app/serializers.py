from rest_framework.serializers import ModelSerializer
from .models import *

class SerializerMachine(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('first_name', 'email')