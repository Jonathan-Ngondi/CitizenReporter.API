from rest_framework import serializers
from .models import Responses
from django.contrib.auth.models import User

class ResponsesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Responses
        fields = ('id', 'created', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')
        read_only_fields = ('created', 'id',)

class UserSerializer(serializers.ModelSerializer):
    '''Serializer to map the User model into JSON format'''

    class Meta:
        model = User