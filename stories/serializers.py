from rest_framework import serializers
from .models import Responses

class ResponsesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    media = serializers.FileField(max_length=None, use_ulr=True)
    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Responses
        fields = ('id', 'created', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')
        read_only_fields = ('created', 'id',)