from django.shortcuts import render, redirect
from .models import Users
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from roadmap.models import Users
from roadmap.serializers import RegisterSerializer

@csrf_exempt
def SignUp(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def SignIn(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)