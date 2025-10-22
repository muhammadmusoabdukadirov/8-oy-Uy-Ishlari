from django.db import models

class Restoran(models.Model):
    nom = models.CharField(max_length=200, verbose_name="Restoran nomi")
    manzil = models.CharField(max_length=255, verbose_name="Manzil")
    telefon = models.CharField(max_length=20, verbose_name="Telefon raqami")
    ochilish_vaqti = models.TimeField(verbose_name="Ochiladi")
    yopilish_vaqti = models.TimeField(verbose_name="Yopiladi")
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Restoran"
        verbose_name_plural = "Restoranlar"


class Menyu(models.Model):
    restoran = models.ForeignKey(Restoran, on_delete=models.CASCADE, related_name="menyular", verbose_name="Restoran")
    nom = models.CharField(max_length=200, verbose_name="Menyu nomi")
    tavsif = models.TextField(verbose_name="Tavsif", blank=True)
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"{self.nom} ({self.restoran.nom})"

    class Meta:
        verbose_name = "Menyu"
        verbose_name_plural = "Menyular"


class Idish(models.Model):
    menyu = models.ForeignKey(Menyu, on_delete=models.CASCADE, related_name="idishlar", verbose_name="Menyu")
    nom = models.CharField(max_length=200, verbose_name="Idish nomi")
    narx = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    mavjud = models.BooleanField(default=True, verbose_name="Mavjudmi?")
    tavsif = models.TextField(blank=True, verbose_name="Tavsif")

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Idish"
        verbose_name_plural = "Idishlar"


class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=100, verbose_name="Ism")
    familiya = models.CharField(max_length=100, verbose_name="Familiya")
    telefon = models.CharField(max_length=20, verbose_name="Telefon raqami")
    manzil = models.CharField(max_length=255, verbose_name="Manzil")
    royxatdan_otgan_sana = models.DateTimeField(auto_now_add=True, verbose_name="Royxatdan otgan sana")

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"


class Buyurtma(models.Model):
    foydalanuvchi = models.ForeignKey(Foydalanuvchi, on_delete=models.CASCADE, related_name="buyurtmalar", verbose_name="Foydalanuvchi")
    idish = models.ForeignKey(Idish, on_delete=models.CASCADE, related_name="buyurtmalar", verbose_name="Idish")
    miqdor = models.PositiveIntegerField(default=1, verbose_name="Miqdor")
    umumiy_narx = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Umumiy narx")
    holat = models.CharField(max_length=50, choices=[
        ('yangi', 'Yangi'),
        ('tayyorlanmoqda', 'Tayyorlanmoqda'),
        ('yetkazilmoqda', 'Yetkazilmoqda'),
        ('yakunlandi', 'Yakunlandi')
    ], default='yangi', verbose_name="Holat")
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Buyurtma sanasi")

    def __str__(self):
        return f"{self.foydalanuvchi} - {self.idish.nom}"

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class Haydovchi(models.Model):
    ism = models.CharField(max_length=100, verbose_name="Ism")
    familiya = models.CharField(max_length=100, verbose_name="Familiya")
    telefon = models.CharField(max_length=20, verbose_name="Telefon raqami")
    transport = models.CharField(max_length=50, verbose_name="Transport turi (masalan, motor, mashina)")

    def __str__(self):
        return f"{self.ism} {self.familiya}"

    class Meta:
        verbose_name = "Haydovchi"
        verbose_name_plural = "Haydovchilar"


class YetkazibBerish(models.Model):
    buyurtma = models.OneToOneField(Buyurtma, on_delete=models.CASCADE, related_name="yetkazish", verbose_name="Buyurtma")
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.SET_NULL, null=True, related_name="yetkazilgan_buyurtmalar", verbose_name="Haydovchi")
    manzil = models.CharField(max_length=255, verbose_name="Yetkazib berish manzili")
    yetkazilgan_vaqt = models.DateTimeField(null=True, blank=True, verbose_name="Yetkazilgan vaqt")

    def __str__(self):
        return f"{self.buyurtma} - {self.haydovchi}"

    class Meta:
        verbose_name = "Yetkazib berish"
        verbose_name_plural = "Yetkazib berishlar"


class Tolov(models.Model):
    buyurtma = models.OneToOneField(Buyurtma, on_delete=models.CASCADE, related_name="tolov", verbose_name="Buyurtma")
    summa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tolov summasi")
    usul = models.CharField(max_length=50, choices=[
        ('naqd', 'Naqd'),
        ('karta', 'Karta'),
        ('onlayn', 'Onlayn')
    ], verbose_name="Tolov usuli")
    tolangan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Tolov sanasi")

    def __str__(self):
        return f"{self.buyurtma} - {self.summa} som"

    class Meta:
        verbose_name = "Tolov"
        verbose_name_plural = "Tolovlar"


class KoribChiqish(models.Model):
    foydalanuvchi = models.ForeignKey(Foydalanuvchi, on_delete=models.CASCADE, related_name="fikrlar", verbose_name="Foydalanuvchi")
    idish = models.ForeignKey(Idish, on_delete=models.CASCADE, related_name="fikrlar", verbose_name="Idish")
    reyting = models.PositiveSmallIntegerField(default=5, verbose_name="Reyting (1-5)")
    izoh = models.TextField(blank=True, verbose_name="Izoh")
    yaratilgan_vaqt = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"{self.foydalanuvchi} → {self.idish} ({self.reyting}⭐)"

    class Meta:
        verbose_name = "Korib chiqish"
        verbose_name_plural = "Korib chiqishlar"


class Like(models.Model):
    foydalanuvchi = models.ForeignKey("Foydalanuvchi", on_delete=models.CASCADE)
    idish = models.ForeignKey("Idish", on_delete=models.CASCADE, related_name="likes")
    like = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.foydalanuvchi.ism} -> {self.idish.nom} ({'Like' if self.like else 'Dislike'})"


class Comment(models.Model):
    foydalanuvchi = models.ForeignKey("Foydalanuvchi", on_delete=models.CASCADE)
    idish = models.ForeignKey("Idish", on_delete=models.CASCADE, related_name="comments")
    matn = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.foydalanuvchi.ism} izohi: {self.matn[:20]}..."
