from django.test import TestCase, Client
from django.urls import reverse
from ..models import FishingPlace, Method


class FishingPlaceTest(TestCase):
    def setUp(self):
        self.place = FishingPlace.objects.create(
            name="Gradina Lake", description="Many kind fishes here")

    def test_place_content(self):
        place = self.place
        self.assertEqual(place.name, 'Gradina Lake')
        self.assertEqual(place.description, "Many kind fishes here")


class FishingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.method = Method.objects.create(name="Spining", slug="spining")
        self.place = FishingPlace.objects.create(
            name="Vit River",
            slug='vit-river',
            description="Carp and cockroach",
            place_type="river"
        )
        self.place.methods.add(self.method)

    def test_index_view_pagination(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fishing_app/index.html')
        self.assertContains(response, 'Vit River')

    def test_search_results_success(self):
        response = self.client.get(reverse('search_results'), {'q': 'Vit'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.place, response.content['results'])

    def test_search_no_results(self):
        response = self.client.get(reverse('search_results'), {'q': 'shark'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.content['results']), 0)

    def test_place_detail_404(self):
        response = self.client.get(
            reverse('place_detail', kwargs={'slug': 'No such place'}))
        self.assertEqual(response.status_code, 404)
