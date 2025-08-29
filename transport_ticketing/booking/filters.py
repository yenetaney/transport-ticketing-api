import django_filters
from booking.models import Trip

class TripFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(field_name='company__name', lookup_expr='icontains')
    origin = django_filters.CharFilter(field_name='route__origin', lookup_expr='icontains')
    destination = django_filters.CharFilter(field_name='route__destination', lookup_expr='icontains')
    departure_time = django_filters.DateTimeFilter(field_name='departure_time', lookup_expr='gte')

    class Meta:
        model = Trip
        fields = ['company_name', 'origin', 'destination', 'departure_time']