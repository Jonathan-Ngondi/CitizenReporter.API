from rest_framework import serializers
from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = ('id', 'title', 'description', 'required_media','number_of_responses',
                                                                'deadline',)
                                    