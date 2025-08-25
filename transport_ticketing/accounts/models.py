from django.db import models
from django.contrib.auth.models import AbstractUser
from booking.models import TransportCompany

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('passenger', 'Passenger'),
        ('company_admin', 'Company Admin'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='passenger')
    email = models.EmailField(unique=True)
    company = models.ForeignKey(TransportCompany, null=True, blank=True, on_delete=models.SET_NULL)
