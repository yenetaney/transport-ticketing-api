# serializers.py
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from booking.models import TransportCompany

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role= 'passenger'
        )
        Token.objects.get_or_create(user = user)
        return user
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

class CompanyAdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'company']

    def create(self, validated_data):
        company_name = validated_data.pop('company')
        try:
            company = TransportCompany.objects.get(name=company_name)
        except TransportCompany.DoesNotExist:
            raise serializers.ValidationError({"company": "Company with this name does not exist."})
        
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role='company_admin',
            company=company
        )
        Token.objects.get_or_create(user=user)
        return user
       





            