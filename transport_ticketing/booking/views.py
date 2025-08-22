from django.shortcuts import render
from .models import TransportCompany, Route, Trip
from .serializers import TransportCompanySerializer, RouteSerializer, TripSerializer
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

class TripViewSet(viewsets.ModelViewSet):
     queryset = Trip.objects.all()
     serializer_class = TripSerializer
     permission_classes = [IsAdminOrReadOnly]