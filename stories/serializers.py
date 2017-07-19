from rest_framework import serializers
from .models import Responses

class ResponsesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Responses
        fields = ('id', 'owner', 'created', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')
        read_only_fields = ('created')