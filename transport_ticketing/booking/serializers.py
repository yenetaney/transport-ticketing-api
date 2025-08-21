from rest_framework import serializers
from .models import TransportCompany

class TransportComponySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = ['id','name', 'owner', 'contact_info']
        read_only_fields = ['owner']

        def create(self, validated_data):
            validated_data['owner'] = self.context['request'].user
            return super().create(validated_data)