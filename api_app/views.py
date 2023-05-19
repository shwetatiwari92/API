from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class GetData(APIView):
    def get(self, request, pk):
        user_data =  User.objects.get(id = pk)
        ser_obj = SerializerMachine(user_data)
        d1 = ser_obj.data
        return Response(data= d1)
    

class CreateData(APIView):
    def post(self, request):
        ser_obj = SerializerMachine(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save() #ye method call karne pe database mein row create ho jaayega
            user_data =  User.objects.all()
            ser_obj = SerializerMachine(user_data, many = True)
            d1 = ser_obj.data
            return Response(data= d1)
        else:
            return Response(ser_obj.errors)
        
        
class UpdateData(APIView):
    def put(self, request, pk):
        user_obj = User.objects.get(id = pk)
        ser_obj = SerializerMachine(user_obj, data= request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            user_data =  User.objects.all()
            ser_obj = SerializerMachine(user_data, many = True)
            d1 = ser_obj.data
            return Response(data= d1)
        else:
            return Response(ser_obj.errors)
        

class DeleteData(APIView):
    def delete(self, request, pk):
        user_obj = User.objects.get(id = pk)
        user_obj.delete()
        user_data =  User.objects.all()
        ser_obj = SerializerMachine(user_data, many = True)
        d1 = ser_obj.data
        return Response(data= d1)