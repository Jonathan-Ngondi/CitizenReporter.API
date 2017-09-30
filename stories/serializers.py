from rest_framework import serializers

from stories.models import Media, Story

class ParseStorySerializer(serializers.Serializer):
    created = serializers.DateTimeField()
    local_id = serializers.CharField()
    assignmentId = serializers.CharField(max_length=200)
    title = serializers.CharField()
    summary = serializers.CharField()
    when = serializers.DateTimeField()
    where = serializers.CharField()
    who = serializers.CharField()
    author = serializers.CharField()
    uploaded = serializers.BooleanField()
    updated = serializers.DateTimeField()

    def create(self, validated_data):
         return Story(**validated_data)

class StorySerializer(serializers.ModelSerializer):
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


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('story', 'file')

    def create(self, validated_data):
        story_id = validated_data.pop('story')
        return Media.objects.create(story=story_id, **validated_data)
