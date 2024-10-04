from rest_framework import serializers
from django.contrib.auth import get_user_model

# Serializer for the User model, handling the creation and representation of users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Uses the currently active user model in the project
        fields = ['username', 'email', 'password']  # Fields to include in the serialized output

    # Custom create method to handle user creation
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)  # Creates a new user
        return user
