import json
from django.test import TestCase

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from .models import Headline
from .serializers import HeadlineSerializer

# Create your tests here.
class ListHeadlineAPIViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'title': 'Go to Ibiza', 'url':'https://detik.com/ramadhan2021'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")
    
    def test_api_create_headline(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_1(self):
        response = self.client.get('/', format='json')
        self.assertEqual(response.status_code, 200)
    
    def test_api_get_headline(self):
        headline = Headline.objects.get()
        response = self.client.get(
            reverse('detail',
            kwargs={'pk': headline.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, headline)
    
    def test_api_update_headline(self):
        headline = Headline.objects.get()
        change_headline = {'title': 'Ramadhan 2021', 'category':'ramadhan', 'url':'https://detik.com/ramadhan2021'}
        res = self.client.put(
            reverse('detail', kwargs={'pk': headline.id}),
            change_headline, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_api_delete_headline(self):
        headline = Headline.objects.get()
        response = self.client.delete(
            reverse('detail', kwargs={'pk': headline.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    