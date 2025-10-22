from rest_framework import serializers
from .models import *

class MenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = "__all__"


class RestoranSerializer(serializers.ModelSerializer):
    menyular = MenyuSerializer(many=True, read_only=True)

    class Meta:
        model = Restoran
        fields = "__all__"
        depth = 1 


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ['foydalanuvchi']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        depth = 1


class IdishSerializer(serializers.ModelSerializer):
    like_soni = serializers.SerializerMethodField()
    dislike_soni = serializers.SerializerMethodField()
    comment_soni = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Idish
        fields = "__all__"
        depth = 1

    def get_like_soni(self, obj):
        return obj.likes.filter(like=True).count()

    def get_dislike_soni(self, obj):
        return obj.likes.filter(like=False).count()

    def get_comment_soni(self, obj):
        return obj.comments.count()



class MenyuDetailSerializer(serializers.ModelSerializer):
    idishlar = IdishSerializer(many=True, read_only=True)

    class Meta:
        model = Menyu
        fields = "__all__"
        depth = 1


class BuyurtmaSerializer(serializers.ModelSerializer):
    foydalanuvchi = serializers.PrimaryKeyRelatedField(queryset=Foydalanuvchi.objects.all())
    idish = serializers.PrimaryKeyRelatedField(queryset=Idish.objects.all())

    class Meta:
        model = Buyurtma
        fields = "__all__"


class FoydalanuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
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

# -----------------------------------------------------------------------

# 2 darsdagi serializers domla

# class RestoranSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restoran
#         fields = "__all__"

# class MenyuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menyu
#         fields = "__all__"

# class IdishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Idish
#         fields = "__all__"

# class FoydalanuvchiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Foydalanuvchi
#         fields = "__all__"

# class BuyurtmaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Buyurtma
#         fields = "__all__"

# class HaydovchiSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Haydovchi
#         fields = "__all__"

# class YetkazibBerishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = YetkazibBerish
#         fields = "__all__"

# class TolovSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tolov
#         fields = "__all__"

# class KoribChiqishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = KoribChiqish
#         fields = "__all__"


# -----------------------------------------------------------------------

# 1 darsdegi serializers domla

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
