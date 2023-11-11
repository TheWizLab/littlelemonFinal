from django.test import TestCase, Client
from LittleLemonAPI.models import MenuItem, Category
from decimal import Decimal
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from LittleLemonAPI import views

class MenuViewtest(TestCase):
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.cat = Category.objects.create(title='random', slug='random')
        self.icecream = MenuItem.objects.create(title="IceCream", price=80, inventory=10, featured=False, category_id=1)

    def loginAsTestUser(self):
        self.client.login(
            username='testuser',
            password='testpassword'
        )

    def test_view_auth(self):
        response = self.client.get(reverse('msg'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('msg'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_getall(self):

        pass