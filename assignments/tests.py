from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from assignments.models import Assignment


class BaseTestCase(APITestCase):
    
    def setUp(self):
        self.assignment = Assignment(id=1, title="Tester", 
                            description="A test case for us", required_media="Video",
                            deadline="2017-08-23")

# Create your tests here.

class CRUDTestCase(BaseTestCase):
    """
    This series of tests, test the basic CRUD functionality of the assignments API.
    """
    def test_post_method_for_assignments(self):
        url = reverse('assignments')
        data = {'id':2, 'title':'Test Works!', 'description':"Post method works",
                "required_media":"Image", "deadline":"2017-09-01"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Assignment.objects.count(), 2)

    def test_get_method_for_assignment(self):
        url = reverse('assignments')
        response = self.client.get()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(response.data, 'Tester')
    
    def test_update_method_for_assignments(self):
        url = reverse('assignments/1')
        data = {'id':1, 'title':'Test Works!', 'description':"Put method works",
                "required_media":"Image", "deadline":"2017-09-01"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_assignment = Assignment.objects.get(pk=1)
        assert updated_assignment.title is 'Test Works!'
    
    def test_delete_method_for_assignments(self):
        data = {'id':2, 'title':'Test Works!', 'description':"Post method works",
                "required_media":"Image", "deadline":"2017-09-01"}
        url = reverse('assignments/2')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
