from rest_framework import serializers
from .models import TransportCompany, Route, Trip

class TransportCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = ['id','name', 'owner', 'contact_info']
        read_only_fields = ['owner']

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
    
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'origin', 'destination', 'duration_estimate']
        
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id',  'route', 'company', 'departure_time', 'available_seats', 'price']