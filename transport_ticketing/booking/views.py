from rest_framework.response import Response
from .models import TransportCompany, Route, Trip
from .serializers import TransportCompanySerializer, RouteSerializer, TripSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import viewsets, status

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

     def create(self, request, *args, **kwargs):
         if request.user.role != "admin":
             return Response ({"detail" :"Only admins can create trips."}, status=status.HTTP_403_FORBIDDEN)
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         self.perform_create(serializer)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
            