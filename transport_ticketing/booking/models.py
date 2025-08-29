from django.db import models
from django.conf import settings


# Create your models here.

class TransportCompany(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True,
                              related_name='companies')
    
    contact_info = models.TextField(blank=True) 

    def __str__(self):
        return f'{self.name} ({self.owner.username})'

class Route(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    duration_estimate = models.DurationField()

    def __str__(self):
        return f'{self.origin} → {self.destination}'
    
class Trip(models.Model):
    route = models.ForeignKey('booking.Route', on_delete=models.CASCADE)
    company = models.ForeignKey('booking.TransportCompany', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    available_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.route.origin} → {self.route.destination} at {self.departure_time}"
    
    @property
    def remaining_seats(self):
        booked = self.booking_set.count()
        return self.available_seats - booked

    
class Booking(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default="confirmed")

    class Meta:
        unique_together = ['trip', 'seat_number']

    