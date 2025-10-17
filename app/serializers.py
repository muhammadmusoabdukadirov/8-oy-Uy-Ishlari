from rest_framework import serializers
from .models import *

# Hammasi bir xil formatda
class RestoranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restoran
        fields = "__all__"

class MenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = "__all__"

class IdishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idish
        fields = "__all__"

class FoydalanuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = "__all__"

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = "__all__"

class YetkazibBerishSerializer(serializers.ModelSerializer):
    class Meta:
        model = YetkazibBerish
        fields = "__all__"

class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = "__all__"

class KoribChiqishSerializer(serializers.ModelSerializer):
    class Meta:
        model = KoribChiqish
        fields = "__all__"

# class RestoranSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restoran
#         fields = "__all__"


# class MenyuSerializer(serializers.ModelSerializer):
#     restoran_nom = serializers.CharField(source='restoran.nom', read_only=True)

#     class Meta:
#         model = Menyu
#         fields = "__all__"


# class IdishSerializer(serializers.ModelSerializer):
#     menyu_nom = serializers.CharField(source='menyu.nom', read_only=True)
#     restoran_nom = serializers.CharField(source='menyu.restoran.nom', read_only=True)

#     class Meta:
#         model = Idish
#         fields = "__all__"


# class FoydalanuvchiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Foydalanuvchi
#         fields = "__all__"


# class BuyurtmaSerializer(serializers.ModelSerializer):
#     foydalanuvchi_ismi = serializers.CharField(source='foydalanuvchi.ism', read_only=True)
#     idish_nom = serializers.CharField(source='idish.nom', read_only=True)
#     umumiy_hisob = serializers.SerializerMethodField()

#     def get_umumiy_hisob(self, obj):
#         return obj.miqdor * obj.idish.narx

#     class Meta:
#         model = Buyurtma
#         fields = "__all__"


# class HaydovchiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Haydovchi
#         fields = "__all__"


# class YetkazibBerishSerializer(serializers.ModelSerializer):
#     buyurtma_foydalanuvchi = serializers.CharField(source='buyurtma.foydalanuvchi.ism', read_only=True)
#     haydovchi_ismi = serializers.CharField(source='haydovchi.ism', read_only=True)

#     class Meta:
#         model = YetkazibBerish
#         fields = "__all__"


# class TolovSerializer(serializers.ModelSerializer):
#     buyurtma_foydalanuvchi = serializers.CharField(source='buyurtma.foydalanuvchi.ism', read_only=True)

#     class Meta:
#         model = Tolov
#         fields = "__all__"


# class KoribChiqishSerializer(serializers.ModelSerializer):
#     foydalanuvchi_ismi = serializers.CharField(source='foydalanuvchi.ism', read_only=True)
#     idish_nom = serializers.CharField(source='idish.nom', read_only=True)

#     class Meta:
#         model = KoribChiqish
#         fields = "__all__"
