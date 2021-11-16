"""
Test over api clients
"""
import random
from datetime import date, datetime

from faker import Faker

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
# DRF
from rest_framework import status
from rest_framework.test import APIClient
# Models
from api.models import Client, Team, Profile, Sales


class ClientTestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:clients-list')
        self.client_one = Client.objects.create(name='Client ', last_name='One')

    def test_get_list_clients(self):
        """Ger list clients endpoint """
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        """test create client successful"""
        res = self.client.post(self.url, {'name': 'Carlos', 'last_name': 'Marsh'})
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', res.data.keys())

    def test_get_client_by_id(self):
        """Get a specific client by id"""
        url = reverse('api:clients-detail', kwargs={'pk': self.client_one.id})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.client_one.name, res.data['name'])


class UserTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='superadmin',
            first_name='Admin',
        )
        self.user.set_password('qwerty')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_get_users(self):
        res = self.client.get(reverse('api:users-list'))
        print(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_user_by_id(self):
        res = self.client.get(reverse('api:users-detail', kwargs={'pk': self.user.id}))
        print(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class TeamTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='superadmin',
            first_name='Admin',
        )
        self.user.set_password('qwerty')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.team_one = Team.objects.create(name='Brokers')
        Team.objects.create(name='Costumers Center')

    def test_get_list_team(self):
        res = self.client.get(reverse('api:teams-list'))
        # print(res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_team_detailt(self):
        res = self.client.get(reverse('api:teams-detail', kwargs={'slug_name': self.team_one.slug_name}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class SalesTest(TestCase):
    """TOTO -> Test over sales endpoint and  check stats"""

    def setUp(self):
        self.client = APIClient()
        self.faker = Faker()
        for _ in range(3):
            Team.objects.create(
                name=self.faker.domain_word()
            )
        for _ in range(7):
            self.create_user()
        for _ in range(25):
            self.create_client()
        for _ in range(100):
            self.create_sales()

    def test_get_sales_by_user(self):
        """Sales by a specific user  """
        user = get_user_model().objects.order_by('?')[0]

        sales = Sales.objects.filter(user=user).count()
        res = self.client.get(
            reverse('api:sales-user-list', kwargs={'user_id': user.pk}),
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], sales)

    def test_get_sales_by_not_existed_user(self):
        """Try to get sales for a non-existed user"""
        res = self.client.get(
            reverse('api:sales-user-list', kwargs={'user_id': 1000}),
        )
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def create_client(self):
        return Client.objects.create(
            name=self.faker.first_name(),
            last_name=self.faker.last_name()
        )

    def create_user(self):
        user = get_user_model().objects.create(
            username=self.faker.simple_profile()['username'],
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            email=self.faker.free_email()
        )
        profile = Profile.objects.create(
            user=user,
            team=Team.objects.order_by('?')[0]
        )
        return user, profile

    def create_sales(self):
        return Sales.objects.create(
            client=Client.objects.order_by('?')[0],
            user=get_user_model().objects.order_by('?')[0],
            date=self.faker.date(),
            amount=random.randrange(1, 1000, 2)
        )
