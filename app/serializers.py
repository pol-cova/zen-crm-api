from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer as DjoserUserSerializer
from .models import User


class CustomUserCreateSerializer(UserCreateSerializer):
    re_password = serializers.CharField(write_only=True)
    is_owner = serializers.BooleanField(required=False)
    business_name = serializers.CharField(required=False, allow_null=True)
    type_of_business = serializers.CharField(required=False, allow_null=True)
    size_of_business = serializers.CharField(required=False, allow_null=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'username', 'password', 're_password',
                  'is_owner', 'business_name', 'type_of_business',
                  'size_of_business']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Remove re_password as it's only for validation
        validated_data.pop('re_password', None)

        # Ensure business fields are explicitly handled
        is_owner = validated_data.get('is_owner', False)
        business_name = validated_data.get('business_name')
        type_of_business = validated_data.get('type_of_business')
        size_of_business = validated_data.get('size_of_business')

        # Create the user with base fields
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            is_owner=is_owner,
            business_name=business_name,
            type_of_business=type_of_business,
            size_of_business=size_of_business
        )
        return user

class CustomUserSerializer(DjoserUserSerializer):
    is_owner = serializers.BooleanField(required=False)
    business_name = serializers.CharField(required=False, allow_null=True)
    type_of_business = serializers.CharField(required=False, allow_null=True)
    size_of_business = serializers.CharField(required=False, allow_null=True)

    class Meta(DjoserUserSerializer.Meta):
        model = User
        fields = ['email', 'username', 'is_owner', 'business_name',
                  'type_of_business', 'size_of_business']
        read_only_fields = ('email',)