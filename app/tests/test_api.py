from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from app.models import Restoran, Menyu
from app.serializers import RestoranSerializer, MenyuSerializer


class RestoranAPITestCase(APITestCase):
    def setUp(self):
        self.restoran1 = Restoran.objects.create(
            nom='Oshxona',
            manzil='Sergeli',
            telefon='998901234567',
            ochilish_vaqti='09:00',
            yopilish_vaqti='22:00'
        )
        self.restoran2 = Restoran.objects.create(
            nom='Choyxona',
            manzil='Chilonzor',
            telefon='998998887766',
            ochilish_vaqti='10:00',
            yopilish_vaqti='23:00'
        )

    def test_get_all_restorans(self):
        url = reverse('restoran-list')
        response = self.client.get(url)

        serializer = RestoranSerializer([self.restoran1, self.restoran2], many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_restoran_by_name(self):
        url = reverse('restoran-list')
        response = self.client.get(url, {'nom': 'Oshxona'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(r['nom'] == 'Oshxona' for r in response.data))


class MenyuAPITestCase(APITestCase):
    def setUp(self):
        self.restoran = Restoran.objects.create(
            nom='FastFood',
            manzil='Chilonzor',
            telefon='998901122334',
            ochilish_vaqti='08:00',
            yopilish_vaqti='23:30'
        )

        self.menyu1 = Menyu.objects.create(restoran=self.restoran, nom='Burgerlar', tavsif='Yumshoq nonli burgerlar')
        self.menyu2 = Menyu.objects.create(restoran=self.restoran, nom='Ichimliklar', tavsif='Sovuq ichimliklar')

    def test_get_all_menus(self):
        url = reverse('menyu-list')
        response = self.client.get(url)
        serializer = MenyuSerializer([self.menyu1, self.menyu2], many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_menu_by_name(self):
        url = reverse('menyu-list')
        response = self.client.get(url, {'nom': 'Burgerlar'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(m['nom'] == 'Burgerlar' for m in response.data))
