from django.shortcuts import render

import json
import bcrypt
import jwt

from .models         import User
from roadmap.settings import SECRET_KEY
from django.views    import View
from django.http     import HttpResponse, JsonResponse

# Create your views here.

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message" : "EXISTS_EMAIL"}, status=400)
            
            User.objects.create(
                username = data['username'],
                email 	 = data['email'], 
                password = bcrypt.hashpw(data["password"].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")
            ).save()

            return HttpResponse(status=200)
            
        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status=400)

class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if User.objects.filter(email=data["email"]).exists():
                user = User.objects.get(email=data["email"])

                if bcrypt.checkpw(data['password'].encode('UTF-8'), user.password.encode('UTF-8')):

                    token = jwt.encode({'user' : user.id}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
                    
                    return JsonResponse({"token" : token}, status=200)

                return HttpResponse(status=401)

            return HttpResponse(status=400)
        
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status=400)