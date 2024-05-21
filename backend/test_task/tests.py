from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestRoutes(TestCase):
    def test_home_page(self):
        url = reverse('test_task:input_response')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestTask(TestCase):
    def test_task_URL(self):
        url = reverse('test_task:get_task')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
