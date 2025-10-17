from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('restoranlar', RestoranViewSet)
router.register('menyular', MenyuViewSet)
router.register('idishlar', IdishViewSet)
router.register('foydalanuvchilar', FoydalanuvchiViewSet)
router.register('buyurtmalar', BuyurtmaViewSet)
router.register('haydovchilar', HaydovchiViewSet)
router.register('yetkazishlar', YetkazibBerishViewSet)
router.register('tolovlar', TolovViewSet)
router.register('fikrlar', KoribChiqishViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
