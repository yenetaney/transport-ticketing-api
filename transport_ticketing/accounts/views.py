from rest_framework import generics
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserPromotionSerializer
from .permissions import IsSuperAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self,request,  *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(id=response.data['id'])
        token, _ = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # creates a session
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "Login successful",
                            "username": user.username,
                            "token" : token.key,
                            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsSuperAdmin]

class UserPromotionView(APIView):
    permission_classes = [IsSuperAdmin]

    def post(self, request):
        print("Raw request data:", request.data)

        serializer = UserPromotionSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            company = user.company  # now linked after save
            return Response({
                "message": f"{user.username} has been promoted to company admin for {company.name}."
            })
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=400)
    
