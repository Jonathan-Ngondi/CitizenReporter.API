from rest_framework import serializers
from .models import Response, Media

class ResponseSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    media = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Story
        fields = (
            'id', 'created', 'local_id', 'title', 'summary', 'when', 'where',
            'who', 'author', 'fb_id', 'media', 'uploaded', 'updated',
            "local_media_paths")
        read_only_fields = ('created', 'id', 'media')


    def create(self, validate_data):
        responses = Response.objects.latest('created_at')
        media = validate_data.pop('media')
        for file in media:
            media_files = Media.objects.create(media=file,responses=responses,**validate_data)
        return media_files

class UserStoriesSerializer(serializers.ModelSerializer):
    media = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Story
        fields = (
            'id', 'created', 'local_id', 'title', 'summary', 'when', 'where',
            'who', 'author', 'fb_id', 'media', 'uploaded',
            "local_media_paths", 'updated')
        read_only_fields = ('created', 'id', 'media')
        lookup_field = 'fb_id'


<<<<<<< HEAD


=======
>>>>>>> refactor of stories model
class MediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Media
        read_only_fields = ("response",)

