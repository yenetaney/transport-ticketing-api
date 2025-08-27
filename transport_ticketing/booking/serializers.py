from rest_framework import serializers
from .models import TransportCompany, Route, Trip
from accounts.models import CustomUser

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
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Trip
        fields = ['id',  'route', 'company', 'departure_time','company_name', 'available_seats', 'price']
        read_only_fields = ['company']
