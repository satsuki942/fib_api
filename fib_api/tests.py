from django.test import TestCase, Client
from django.urls import reverse
from urllib.parse import urlencode
from rest_framework import status
from .views import fib,FibResult

# Create your tests here.

class FibNViewTest(TestCase):
    def test_get_success(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'n':10})}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_failed1(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'b':10})}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_get_failed2(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'n':0})}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_get_failed3(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'n':'str'})}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_get_data1(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'n':10})}'
        response = self.client.get(url)
        json_code = {
            "result":55
        }
        self.assertEqual(response.data, json_code)

    def test_get_data2(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'b':10})}'
        response = self.client.get(url)
        json_code = {
            "status":400,
            "message":"Bad Request: Request parameter name is not appropriate"
        }
        self.assertEqual(response.data, json_code)

    def test_get_data3(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'n':0})}'
        response = self.client.get(url)
        json_code = {
            "status":400,
            "message":"Bad Request: Parameter value is less than 1"
        }
        self.assertEqual(response.data, json_code)

    def test_get_data4(self):
        base_url = reverse('fib')
        url = f'{base_url}?{urlencode({'n':'str'})}'
        response = self.client.get(url)
        json_code = {
            "status":400,
            "message":"Bad Request: Given request parameter value is NaN, int value is required"
        }
        self.assertEqual(response.data, json_code)

class fibfuncTest(TestCase):
    def test_fib_success1(self):
        self.assertEqual(fib(1),1)
    
    def test_fib_success2(self):
        self.assertEqual(fib(10),55)

    def test_fib_failed(self):
        with self.assertRaises(ValueError):
            fib(0)

class FibResultTest(TestCase):
    def setUp(self):
        self.result1 = FibResult(400,'message')
        self.result2 = FibResult(200,34)
        self.result3 = FibResult(500,'Hello')

    def test_make_json1(self):
        json_code = {
            "status":400,
            "message":"message"
        }
        self.assertEqual(self.result1.generate_json(),json_code)

    def test_make_json2(self):
        json_code = {
            "result":34
        }
        self.assertEqual(self.result2.generate_json(),json_code)

    def test_make_json3(self):
        json_code = {
            "status":500,
            "message":"Hello"
        }
        self.assertEqual(self.result3.generate_json(),json_code)

    def test_get_http_status1(self):
        self.assertEqual(self.result1.get_http_status(),status.HTTP_400_BAD_REQUEST)

    def test_get_http_status2(self):
        self.assertEqual(self.result2.get_http_status(),status.HTTP_200_OK)

    def test_get_http_status3(self):
        with self.assertRaises(KeyError):
            self.result3.get_http_status()
