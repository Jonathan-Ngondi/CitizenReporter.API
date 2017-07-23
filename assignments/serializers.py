from rest_framework import serializers

from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    """
    This is a serializer for the Assignment model.
    """

    class Meta:
        model = Assignment
        fields = ('id', 'title', 'description', 'required_media',
                  'featured_image', 'number_of_responses', 'deadline',
                  'author', 'assignment_location')
        read_only_fields = ('number_of_responses',)
