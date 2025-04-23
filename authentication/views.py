# authentication/views.py
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        nickname = request.data.get("nickname")
        password = request.data.get("password")
        user = authenticate(request, nickname=nickname, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid nickname or password"}, status=status.HTTP_401_UNAUTHORIZED)
