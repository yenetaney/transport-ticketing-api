from django.db import models
from django.conf import settings

# Create your models here.

class TransportCompany(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='companies')
    contact_info = models.TextField(blank=True) 

    def __str__(self):
        return f'{self.name} ({self.owner.username})'   

