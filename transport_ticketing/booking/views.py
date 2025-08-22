from django.shortcuts import render
from .models import TransportCompany, Route
from .serializers import TransportCompanySerializer, RouteSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import viewsets

# Create your views here.

class TransportCompanyViewSet(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrReadOnly]