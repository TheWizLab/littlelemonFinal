#TestCase class
from django.test import TestCase
from LittleLemonAPI.models import MenuItem, Category


class MenuItemTest(TestCase):
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")

        pass

    def test_get_item(self):
        cat = Category.objects.create(title='random', slug='random')
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=10, featured=False, category_id=1)
        self.assertEqual(item.price, 80)