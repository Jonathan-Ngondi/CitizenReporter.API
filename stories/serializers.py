from rest_framework import serializers
from models import Responses

class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = ('id', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')