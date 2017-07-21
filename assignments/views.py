from rest_framework import generics

from assignments.models import Assignment
from assignments.serializers import AssignmentSerializer


class AssignmentList(generics.ListCreateAPIView):
    """
    Allows you to view all Assignments, also let's you post one
    assignment and add itto the database.
    """

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allows you to view an individual Assignment, update one as well as delete
    an individual assignment.
    """

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
