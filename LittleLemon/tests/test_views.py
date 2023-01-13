from django.test import TestCase
from Restaurant.models import MenuItem
from Restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Pancake", price=12, inventory=22)
        MenuItem.objects.create(title="Soup", price=21, inventory=16)

    def test_getall(self):
        items = MenuItem.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(MenuSerializer(items, many=True).data, serialized_items.data)