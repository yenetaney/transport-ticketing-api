from rest_framework import serializers
from .models import TransportCompany, Route, Trip, Booking


class TransportCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportCompany
        fields = ['id','name' ,'contact_info']

    def create(self, validated_data):
        return TransportCompany.objects.create(**validated_data)

    
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'origin', 'destination', 'duration_estimate']
        
class TripSerializer(serializers.ModelSerializer):
    bookings_count = serializers.SerializerMethodField()
    company_name = serializers.CharField(source='company.name', read_only=True)
    remaining_seats = serializers.SerializerMethodField()


    class Meta:
        model = Trip
        fields = ['id',  'route', 'company', 'departure_time','company_name',
                   'available_seats', 'price', 'bookings_count', 'remaining_seats']
        read_only_fields = ['company']

    def get_bookings_count(self, obj):
        return obj.booking_set.count()

    def get_remaining_seats(self, obj):
        return obj.remaining_seats
    
class BookingSerializer(serializers.ModelSerializer):
    trip_info = TripSerializer(source='trip', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'trip', 'trip_info', 'user', 'seat_number', 'status']
        read_only_fields = ['user', 'status']

    def validate_seat_number(self, value):
        trip = self.initial_data.get('trip')
        try:
            trip_obj = Trip.objects.get(id=trip)
        except Trip.DoesNotExist:
            raise serializers.ValidationError("Trip does not exist.")

        if value > trip_obj.available_seats:
            raise serializers.ValidationError(f"Seat number exceeds available seats ({trip_obj.available_seats}).")

        return value
    def perform_destroy(self, instance):
        instance.status = "cancelled"
        instance.save()

    def get_queryset(self):
        user = self.request.user
        if user.role == "passenger":
            return Booking.objects.filter(user=user)
        elif user.role == "company_admin":
            return Booking.objects.filter(trip__company=user.company)
        elif user.role == "super_admin":
            return Booking.objects.all()
        return Booking.objects.none()
