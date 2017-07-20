from rest_framework import serializers

from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    """This is a serializer for the Assignment model"""
    class Meta:
        model = Assignment
        fields = ('id', 'title', 'description', 'required_media', 'media_upload',
                  'number_of_responses', 'deadline', 'author', 'assignment_location')
