from django.test import TestCase
from .models import Event

class EventModelTest(TestCase):

    def test_string_representation(self):
        event = Event(name="My event")
        self.assertEqual(str(event), event.name)