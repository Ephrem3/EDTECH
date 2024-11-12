from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password

class AuthenticationTests(APITestCase):

    def setUp(self):
        
        self.user_data = {
            'NETID': 'testuser',
            'password': 'testpassword',
        }
        self.user = User.objects.create(
            NETID=self.user_data['NETID'],
            password=make_password(self.user_data['password'])
        )

        self.register_url = '/user/register/'
        self.login_url = '/user/login/'
        self.logout_url = '/user/logout/'

    def test_register_success(self):
        data = {
            'NETID': 'newuser',
            'password': 'newpassword'
        }
        response = self.client.post(self.register_url, data, format='json')
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       # self.assertEqual(response.data['NETID'], 'newuser')

    def test_login_success(self):
        data = {
            'NETID': self.user_data['NETID'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)

    def test_login_failure_invalid_password(self):
        data = {
            'NETID': self.user_data['NETID'],
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'Incorrect Password')

    def test_login_failure_account_not_found(self):
        data = {
            'NETID': 'nonexistentuser',
            'password': 'somepassword'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'Account does  not exist')

    