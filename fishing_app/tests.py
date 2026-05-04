from django.test import TestCase
from .models import FishingPlace


class FishingPlaceTest(TestCase):
    def setUp(self):
        self.place = FishingPlace.objects.create(
            name="Gradina Lake", description="Many kind of fishes here")

    def test_place_content(self):
        place = self.place
        self.assertEqual(place.name, 'Gradina Lake')
        self.assertEqual(place.description, "Many kind fishes here")

    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
