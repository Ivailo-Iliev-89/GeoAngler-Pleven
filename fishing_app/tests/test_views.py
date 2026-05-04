from django.test import TestCase, Client
from django.urls import reverse
from fishing_app.models import FishingPlace, Method


class FishingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.method = Method.objects.create(name="Feeder", slug="feeder")
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
        self.assertIn(self.place, response.context['places'])

    def test_search_results_by_fish_name(self):
        from fishing_app.models import Fish
        carp = Fish.objects.create(name='carp')
        self.place.fishes.add(carp)

        response = self.client.get(reverse('search_results'), {'q': 'carp'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.place, response.context['results'])

    def test_search_results_by_fishing_method(self):
        response = self.client.get(reverse('search_results'), {'q': 'Feeder'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.place, response.context['results'])

    def test_search_no_results(self):
        response = self.client.get(reverse('search_results'), {'q': 'shark'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 0)

    def test_place_detail_404(self):
        response = self.client.get(
            reverse('place_detail', kwargs={'slug': 'no-such-place'}))
        self.assertEqual(response.status_code, 404)
