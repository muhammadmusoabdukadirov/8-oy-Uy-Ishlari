from rest_framework import viewsets, filters
from .models import Restoran, Menyu, Idish, Foydalanuvchi, Buyurtma, Haydovchi, YetkazibBerish, Tolov, KoribChiqish
from .serializers import (
    RestoranSerializer, MenyuSerializer, IdishSerializer, 
    FoydalanuvchiSerializer, BuyurtmaSerializer, HaydovchiSerializer, 
    YetkazibBerishSerializer, TolovSerializer, KoribChiqishSerializer
)

class RestoranViewSet(viewsets.ModelViewSet):
    queryset = Restoran.objects.all()
    serializer_class = RestoranSerializer

class MenyuViewSet(viewsets.ModelViewSet):
    queryset = Menyu.objects.all()
    serializer_class = MenyuSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'tavsif']

class IdishViewSet(viewsets.ModelViewSet):
    queryset = Idish.objects.all()
    serializer_class = IdishSerializer

class FoydalanuvchiViewSet(viewsets.ModelViewSet):
    queryset = Foydalanuvchi.objects.all()
    serializer_class = FoydalanuvchiSerializer

class BuyurtmaViewSet(viewsets.ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer

class HaydovchiViewSet(viewsets.ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer

class YetkazibBerishViewSet(viewsets.ModelViewSet):
    queryset = YetkazibBerish.objects.all()
    serializer_class = YetkazibBerishSerializer

class TolovViewSet(viewsets.ModelViewSet):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer

class KoribChiqishViewSet(viewsets.ModelViewSet):
    queryset = KoribChiqish.objects.all()
    serializer_class = KoribChiqishSerializer
