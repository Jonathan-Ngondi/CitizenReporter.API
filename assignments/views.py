from assignments.models import Assignment
from rest_framework import generics
from assignments.serializers import AssignmentSerializer


class AssignmentList(generics.ListCreateAPIView):
    
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Allows you to view an individual Assignment, update one as well as delete an 
       an individual assignment.
    """
    
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
