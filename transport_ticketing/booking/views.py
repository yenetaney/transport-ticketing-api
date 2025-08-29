from rest_framework.response import Response
from .models import TransportCompany, Route, Trip, Booking
from .serializers import TransportCompanySerializer, RouteSerializer, TripSerializer, BookingSerializer
from .permissions import IsSuperAdminOnly, IsAdminOrReadOnly, CanManageOwnCompanyObject
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from booking.filters import TripFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# Create your views here.

class TransportCompanyViewSet(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer
    permission_classes = [IsSuperAdminOnly]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrReadOnly, CanManageOwnCompanyObject]

class TripViewSet(viewsets.ModelViewSet):
     queryset = Trip.objects.all()
     serializer_class = TripSerializer
     permission_classes = [IsAdminOrReadOnly, CanManageOwnCompanyObject]
     filter_backends = [DjangoFilterBackend, OrderingFilter]
     filterset_class = TripFilter
     ordering_fields = ['departure_time', 'price']

     def create(self, request, *args, **kwargs):
        user = request.user

        if user.role not in ["super_admin", "company_admin"]:
            return Response({"detail": "Only admins can create trips."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company = user.company if user.role == "company_admin" else serializer.validated_data.get("company")
        serializer.save(company=company)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


     def get_queryset(self):
        user = self.request.user
        if user.role == "super_admin":
            return Trip.objects.all()
        elif user.role == "company_admin":
            return Trip.objects.filter(company=user.company)
        elif user.role == "passenger":
            return Trip.objects.all()  
        return Trip.objects.none()
     
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "passenger":
            return Booking.objects.filter(user=user)
        elif user.role == "company_admin":
            return Booking.objects.filter(trip__company=user.company)
        elif user.role == "super_admin":
            return Booking.objects.all()
        return Booking.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="confirmed")