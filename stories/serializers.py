from rest_framework import serializers
from .models import Responses, Media

class ResponsesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Responses
        fields = ('id', 'created', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')
        read_only_fields = ('created', 'id',)

class FileListSerializer(serializers.Serializer):
     media = serializers.ListField(child=serializers.FileField(max_length=None,use_url=True))

     def create(self, validate_data):
         responses = Responses.objects.latest('created_at')
         media = validate_data.pop('media')
         for file in media:
             media_files = Media.objects.create(media=file,responses=responses,**validate_data)
         return media_files

class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        read_only_fields = ("response",)

class UserStoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Responses
        fields = ('id', 'created', 'title', 'why', 'when', 'where', 'who', 'author', 'author_id', 'media')
        read_only_fields = ('created', 'id',)
    
