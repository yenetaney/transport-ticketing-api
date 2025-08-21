from django.shortcuts import render
from .models import TransportCompany
from .serializers import TransportComponySerializer
from .permissions import IsAdminUser
from rest_framework import viewsets

# Create your views here.

class TransportComponyViewSet(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportComponySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
