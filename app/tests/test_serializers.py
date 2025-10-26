from rest_framework.test import APITestCase
from app.models import Restoran, Menyu
from app.serializers import RestoranSerializer, MenyuSerializer

class RestoranSerializerTest(APITestCase):
    def test_restoran_serializer(self):
        restoran = Restoran.objects.create(
            nom='Oshmarkazi',
            manzil='Toshkent, Chilonzor',
            telefon='998901234567',
            ochilish_vaqti='09:00',
            yopilish_vaqti='23:00'
        )

        data = {
            'id': restoran.id,
            'nom': 'Oshmarkazi',
            'manzil': 'Toshkent, Chilonzor',
            'telefon': '998901234567',
            'ochilish_vaqti': '09:00:00',
            'yopilish_vaqti': '23:00:00',
            'yaratilgan_vaqt': restoran.yaratilgan_vaqt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }

        serializer = RestoranSerializer(restoran)
        self.assertEqual(serializer.data['nom'], data['nom'])
        self.assertEqual(serializer.data['telefon'], data['telefon'])


class MenyuSerializerTest(APITestCase):
    def test_menyu_serializer(self):
        restoran = Restoran.objects.create(
            nom='Lag‘monchi',
            manzil='Yunusobod',
            telefon='998991112233',
            ochilish_vaqti='08:00',
            yopilish_vaqti='22:00'
        )

        menyu = Menyu.objects.create(
            restoran=restoran,
            nom='Milliy taomlar',
            tavsif='Mazali oshlar'
        )

        serializer = MenyuSerializer(menyu)
        self.assertEqual(serializer.data['nom'], 'Milliy taomlar')
        self.assertEqual(serializer.data['restoran'], restoran.id)


#malumotlarni chatGPT dan oldim domla qolgani o`zimniki