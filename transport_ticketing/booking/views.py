from django.shortcuts import render
from .models import TransportCompany
from .serializers import TransportCompanySerializer
from .permissions import IsAdminUser
from rest_framework import viewsets

# Create your views here.

class TransportCompanyViewSet(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)