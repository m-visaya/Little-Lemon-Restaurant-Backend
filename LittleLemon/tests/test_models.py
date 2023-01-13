from django.test import TestCase
from Restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price=20, inventory=20)
        item = str(item)
        self.assertEqual(item, "Ice Cream : 20")