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

class UserPromotionSerializer(serializers.Serializer):
    username = serializers.CharField()
    company = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        company_name = data.get('company')

        if not username or not isinstance(username, str) or username.strip() == "":
            raise serializers.ValidationError({"username": "This field is required and must be a non-empty string."})

        if not company_name or not isinstance(company_name, str) or company_name.strip() == "":
            raise serializers.ValidationError({"company": "This field is required and must be a non-empty string."})

        try:
            user = CustomUser.objects.get(username=username.strip())
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({"username": "User not found."})

        try:
            company = TransportCompany.objects.get(name=company_name.strip())
        except TransportCompany.DoesNotExist:
            raise serializers.ValidationError({"company": "Company not found."})

        data['user'] = user
        data['company_obj'] = company
        return data
    
    def save(self):
        user = self.validated_data['user']
        company = self.validated_data['company_obj']
        user.role = 'company_admin'
        user.company = company
        user.save()
        return user