from rest_framework import serializers
from .models import Responses

class ResponsesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Responses
        fields = ('id', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')