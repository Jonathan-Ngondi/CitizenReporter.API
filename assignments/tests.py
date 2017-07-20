
from django.test import TestCase, override_settings
from django.urls import reverse
import tempfile
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from assignments.models import Assignment


def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file

class BaseTestCase(TestCase):

    def setUp(self):
        self.assignment = Assignment(id=1, title="Tester",
                                     description="A test case for us", required_media="Video",
                                     deadline="2017-08-23")

    def test_model_assignment_title(self):
        assert "Tester" in self.assignment.title


class CRUDTestCase(APITestCase):
    """
    This series of tests, test the basic CRUD functionality of the assignments API.
    """

    def test_post_method_for_assignments(self):
        url = reverse('list')
        data = {'id': 2, 'title': 'Test Works!', 'description': "Post method works",
                "required_media": "Image", "deadline": "2017-09-01", "number_of_responses": 4,
                "author": "Tester Mctesty", "location": "Nairobi,Kenya"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Assignment.objects.count(), 1)

    def test_get_method_for_assignment(self):
        url = reverse('list')
        data = {'title': 'Test Works!', 'description': "Post method works",
                "deadline": "2017-09-01", "number_of_responses": 4}
        response = self.client.post(url, data, format='json')
        url = reverse('list')
        response = self.client.get(url)
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Works', data[0]['title'])

    def test_update_method_for_assignments(self):
        url_1 = reverse('list')
        data = {'title': 'Test Works!', 'description': "Post method works",
                "deadline": "2017-09-01", "number_of_responses": 4,
                "author": "Tester Mctesty", "location": "Nairobi,Kenya"}
        self.client.post(url_1, data, format='json')
        url_2 = reverse('detail', args=(1,))
        data = {'title': 'Put Works!', 'description': "Put method works",
                "required_media": "Image", "deadline": "2017-09-01"}
        response = self.client.put(url_2, data, format='json')
        response = self.client.get(url_1)
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Put Works', data[0]['title'])

    def test_delete_method_for_assignments(self):
        data = {'title': 'Test Works!', 'description': "Post method works",
                "number_of_responses": 4, "deadline": "2017-09-01",
                "author": "Tester Mctesty", "location": "Nairobi,Kenya"}
        url = reverse('list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = reverse('detail', args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_upload_picture_method(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        data = {'title': 'Test Works!', 'description': "Post method works",
                "number_of_responses": 4, "deadline": "2017-09-01", "media_upload":test_image,
                "author": "Tester Mctesty", "location": "Nairobi,Kenya"}
        url = reverse('list')
        response = self.client.post(url, data, format='json')
        data = response.data
        import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('.jpg', data['media_upload'])     
