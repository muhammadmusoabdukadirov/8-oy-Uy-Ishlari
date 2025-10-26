from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from app.models import Menyu, Restoran
from app.serializers import MenyuSerializer


class MenyuAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)

        self.restoran = Restoran.objects.create(
            nom='Oshxona',
            manzil='Chilonzor',
            telefon='998901234567',
            ochilish_vaqti='09:00',
            yopilish_vaqti='23:00'
        )

        self.menyu1 = Menyu.objects.create(restoran=self.restoran, nom='Milliy taomlar', tavsif='Mazali oshlar')
        self.menyu2 = Menyu.objects.create(restoran=self.restoran, nom='Fast Food', tavsif='Burger va fri')

        self.url = reverse('menyu-list')


    def test_search_menyu(self):
        response = self.client.get(self.url, {'search': 'Milliy'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Milliy' in m['nom'] for m in response.data))


    def test_filter_menyu(self):
        response = self.client.get(self.url, {'nom': 'Fast Food'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(m['nom'] == 'Fast Food' for m in response.data))


    def test_session_authentication(self):
        self.client.login(username='testuser', password='12345')
        data = {'restoran': self.restoran.id, 'nom': 'Desertlar', 'tavsif': 'Shirinliklar'}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_token_authentication(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        data = {'restoran': self.restoran.id, 'nom': 'Ichimliklar', 'tavsif': 'Sovuq ichimliklar'}
        response = client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nom'], 'Ichimliklar')


    def test_create_menyu(self):
        data = {'restoran': self.restoran.id, 'nom': 'Salatlar', 'tavsif': 'Yengil ovqatlar'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nom'], 'Salatlar')


    def test_update_menyu(self):
        url_detail = reverse('menyu-detail', args=[self.menyu1.id])
        data = {'restoran': self.restoran.id, 'nom': 'Yangilangan menyu', 'tavsif': 'Tahrir qilingan tavsif'}
        response = self.client.put(url_detail, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nom'], 'Yangilangan menyu')


    def test_partial_update_menyu(self):
        url_detail = reverse('menyu-detail', args=[self.menyu2.id])
        data = {'tavsif': 'Yangi fri bilan burgerlar'}
        response = self.client.patch(url_detail, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tavsif'], 'Yangi fri bilan burgerlar')


    def test_delete_menyu(self):
        url_detail = reverse('menyu-detail', args=[self.menyu1.id])
        response = self.client.delete(url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Menyu.objects.filter(id=self.menyu1.id).exists())
