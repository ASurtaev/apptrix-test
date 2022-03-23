from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.request import Request

from .serializers import PersonSerializer
from .models import Person

@api_view(['POST'])
def person_add(request: Request):
    if request.method == 'POST':
        person_serializer = PersonSerializer(data=request.data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def person_list(request: Request):
    if request.method == 'GET':
        persons = Person.objects.all()
        persons_serializer = PersonSerializer(persons, many=True)
        return JsonResponse(persons_serializer.data, safe=False)
