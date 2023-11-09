#TestCase class
from django.test import TestCase
from LittleLemonAPI.models import MenuItem


class MenuItemTest(TestCase):
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=10, featured=False)
        self.assertEqual(item, "IceCream : 80")