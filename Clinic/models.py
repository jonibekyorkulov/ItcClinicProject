from django.db import models
import datetime
import django
from django.contrib.auth.models import AbstractUser, User


class CustomUser(AbstractUser):
    choices = [
        ('doctor', 'Doctor'),
        ('admin', 'Admin')
    ]
    companyName = models.CharField(max_length=125, null=True, blank=True)
    status = models.CharField(max_length=55, null=True, blank=True, choices=choices)

class Normallash(models.Model):
    x1 = models.FloatField(null=True, blank=True)
    x2 = models.FloatField(null=True, blank=True)
    x3 = models.FloatField(null=True, blank=True)
    x4 = models.FloatField(null=True, blank=True)
    x5 = models.FloatField(null=True, blank=True)
    x6 = models.FloatField(null=True, blank=True)
    x7 = models.FloatField(null=True, blank=True)
    x8 = models.FloatField(null=True, blank=True)
    x9 = models.FloatField(null=True, blank=True)
    x10 = models.FloatField(null=True, blank=True)
    x11 = models.FloatField(null=True, blank=True)
    x12 = models.FloatField(null=True, blank=True)
    x13 = models.FloatField(null=True, blank=True)
    x14 = models.FloatField(null=True, blank=True)
    x15 = models.FloatField(null=True, blank=True)
    x16 = models.FloatField(null=True, blank=True)
    x17 = models.FloatField(null=True, blank=True)
    x18 = models.FloatField(null=True, blank=True)
    x19 = models.FloatField(null=True, blank=True)
    x20 = models.FloatField(null=True, blank=True)
    x21 = models.FloatField(null=True, blank=True)
    x22 = models.FloatField(null=True, blank=True)
    x23 = models.FloatField(null=True, blank=True)
    x24 = models.FloatField(null=True, blank=True)
    x25 = models.FloatField(null=True, blank=True)
    x26 = models.FloatField(null=True, blank=True)
    x27 = models.FloatField(null=True, blank=True)
    x28 = models.FloatField(null=True, blank=True)
    x29 = models.FloatField(null=True, blank=True)
    x30 = models.FloatField(null=True, blank=True)
    x31 = models.FloatField(null=True, blank=True)
    x32 = models.FloatField(null=True, blank=True)
    x33 = models.FloatField(null=True, blank=True)
    x34 = models.FloatField(null=True, blank=True)
    x35 = models.FloatField(null=True, blank=True)
    x36 = models.FloatField(null=True, blank=True)
    x37 = models.FloatField(null=True, blank=True)
    x38 = models.FloatField(null=True, blank=True)
    x39 = models.FloatField(null=True, blank=True)
    x40 = models.FloatField(null=True, blank=True)
    x41 = models.FloatField(null=True, blank=True)
    x42 = models.FloatField(null=True, blank=True)
    x43 = models.FloatField(null=True, blank=True)
    x44 = models.FloatField(null=True, blank=True)
    x45 = models.FloatField(null=True, blank=True)
    x46 = models.FloatField(null=True, blank=True)
    x47 = models.FloatField(null=True, blank=True)
    x48 = models.FloatField(null=True, blank=True)
    x49 = models.FloatField(null=True, blank=True)
    x50 = models.FloatField(null=True, blank=True)
    x51 = models.FloatField(null=True, blank=True)
    x52 = models.FloatField(null=True, blank=True)
    x53 = models.FloatField(null=True, blank=True)
    x54 = models.FloatField(null=True, blank=True)
    x55 = models.FloatField(null=True, blank=True)
    x56 = models.FloatField(null=True, blank=True)
    x57 = models.FloatField(null=True, blank=True)
    x58 = models.FloatField(null=True, blank=True)
    x59 = models.FloatField(null=True, blank=True)
    x60 = models.FloatField(null=True, blank=True)
    x61 = models.FloatField(null=True, blank=True)
    x62 = models.FloatField(null=True, blank=True)
    x63 = models.FloatField(null=True, blank=True)
    x64 = models.FloatField(null=True, blank=True)
    x65 = models.FloatField(null=True, blank=True)
    x66 = models.FloatField(null=True, blank=True)
    x67 = models.FloatField(null=True, blank=True)
    x68 = models.FloatField(null=True, blank=True)
    x69 = models.FloatField(null=True, blank=True)
    x70 = models.FloatField(null=True, blank=True)
    x71 = models.FloatField(null=True, blank=True)
    x72 = models.FloatField(null=True, blank=True)
    x73 = models.FloatField(null=True, blank=True)
    x74 = models.FloatField(null=True, blank=True)
    x75 = models.FloatField(null=True, blank=True)
    x76 = models.FloatField(null=True, blank=True)
    x77 = models.FloatField(null=True, blank=True)
    x78 = models.FloatField(null=True, blank=True)
    x79 = models.FloatField(null=True, blank=True)
    x80 = models.FloatField(null=True, blank=True)
    x81 = models.FloatField(null=True, blank=True)
    x82 = models.FloatField(null=True, blank=True)
    x83 = models.FloatField(null=True, blank=True)
    x84 = models.FloatField(null=True, blank=True)
    x85 = models.FloatField(null=True, blank=True)
    x86 = models.FloatField(null=True, blank=True)
    x87 = models.FloatField(null=True, blank=True)
    x88 = models.FloatField(null=True, blank=True)
    x89 = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"{self.id}"



class Lsimptokompleks(models.Model):
    L= models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return f"{self.L}"

class Creator(models.Model):
    name = models.CharField(max_length=126, null=True, blank=True)
    image = models.ImageField(upload_to='creator', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=26, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name

class Nolbir(models.Model):
    x1 = models.FloatField(null=True, blank=True)
    x2 = models.FloatField(null=True, blank=True)
    x3 = models.FloatField(null=True, blank=True)
    x4 = models.FloatField(null=True, blank=True)
    x5 = models.FloatField(null=True, blank=True)
    x6 = models.FloatField(null=True, blank=True)
    x7 = models.FloatField(null=True, blank=True)
    x8 = models.FloatField(null=True, blank=True)
    x9 = models.FloatField(null=True, blank=True)
    x10 = models.FloatField(null=True, blank=True)
    x11 = models.FloatField(null=True, blank=True)
    x12 = models.FloatField(null=True, blank=True)
    x13 = models.FloatField(null=True, blank=True)
    x14 = models.FloatField(null=True, blank=True)
    x15 = models.FloatField(null=True, blank=True)
    x16 = models.FloatField(null=True, blank=True)
    x17 = models.FloatField(null=True, blank=True)
    x18 = models.FloatField(null=True, blank=True)
    x19 = models.FloatField(null=True, blank=True)
    x20 = models.FloatField(null=True, blank=True)
    x21 = models.FloatField(null=True, blank=True)
    x22 = models.FloatField(null=True, blank=True)
    x23 = models.FloatField(null=True, blank=True)
    x24 = models.FloatField(null=True, blank=True)
    x25 = models.FloatField(null=True, blank=True)
    x26 = models.FloatField(null=True, blank=True)
    x27 = models.FloatField(null=True, blank=True)
    x28 = models.FloatField(null=True, blank=True)
    x29 = models.FloatField(null=True, blank=True)
    x30 = models.FloatField(null=True, blank=True)
    x31 = models.FloatField(null=True, blank=True)
    x32 = models.FloatField(null=True, blank=True)
    x33 = models.FloatField(null=True, blank=True)
    x34 = models.FloatField(null=True, blank=True)
    x35 = models.FloatField(null=True, blank=True)
    x36 = models.FloatField(null=True, blank=True)
    x37 = models.FloatField(null=True, blank=True)
    x38 = models.FloatField(null=True, blank=True)
    x39 = models.FloatField(null=True, blank=True)
    x40 = models.FloatField(null=True, blank=True)
    x41 = models.FloatField(null=True, blank=True)
    x42 = models.FloatField(null=True, blank=True)
    x43 = models.FloatField(null=True, blank=True)
    x44 = models.FloatField(null=True, blank=True)
    x45 = models.FloatField(null=True, blank=True)
    x46 = models.FloatField(null=True, blank=True)
    x47 = models.FloatField(null=True, blank=True)
    x48 = models.FloatField(null=True, blank=True)
    x49 = models.FloatField(null=True, blank=True)
    x50 = models.FloatField(null=True, blank=True)
    x51 = models.FloatField(null=True, blank=True)
    x52 = models.FloatField(null=True, blank=True)
    x53 = models.FloatField(null=True, blank=True)
    x54 = models.FloatField(null=True, blank=True)
    x55 = models.FloatField(null=True, blank=True)
    x56 = models.FloatField(null=True, blank=True)
    x57 = models.FloatField(null=True, blank=True)
    x58 = models.FloatField(null=True, blank=True)
    x59 = models.FloatField(null=True, blank=True)
    x60 = models.FloatField(null=True, blank=True)
    x61 = models.FloatField(null=True, blank=True)
    x62 = models.FloatField(null=True, blank=True)
    x63 = models.FloatField(null=True, blank=True)
    x64 = models.FloatField(null=True, blank=True)
    x65 = models.FloatField(null=True, blank=True)
    x66 = models.FloatField(null=True, blank=True)
    x67 = models.FloatField(null=True, blank=True)
    x68 = models.FloatField(null=True, blank=True)
    x69 = models.FloatField(null=True, blank=True)
    x70 = models.FloatField(null=True, blank=True)
    x71 = models.FloatField(null=True, blank=True)
    x72 = models.FloatField(null=True, blank=True)
    x73 = models.FloatField(null=True, blank=True)
    x74 = models.FloatField(null=True, blank=True)
    x75 = models.FloatField(null=True, blank=True)
    x76 = models.FloatField(null=True, blank=True)
    x77 = models.FloatField(null=True, blank=True)
    x78 = models.FloatField(null=True, blank=True)
    x79 = models.FloatField(null=True, blank=True)
    x80 = models.FloatField(null=True, blank=True)
    x81 = models.FloatField(null=True, blank=True)
    x82 = models.FloatField(null=True, blank=True)
    x83 = models.FloatField(null=True, blank=True)
    x84 = models.FloatField(null=True, blank=True)
    x85 = models.FloatField(null=True, blank=True)
    x86 = models.FloatField(null=True, blank=True)
    x87 = models.FloatField(null=True, blank=True)
    x88 = models.FloatField(null=True, blank=True)
    x89 = models.FloatField(null=True, blank=True)





class ExcelFile(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='Excel input', null=True)
    uploud_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}    {self.file.name}"


class Clas(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return self.name


class Etalon(models.Model):
    L = models.ForeignKey(Lsimptokompleks, on_delete=models.SET_NULL, null=True, blank=True)
    nolbir = models.ForeignKey(Nolbir, on_delete=models.SET_NULL, null=True, blank=True)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE, null=True, blank=True)
    normallash = models.ForeignKey(Normallash, models.SET_NULL, null=True, blank=True)
    x1 = models.FloatField(null=True, blank=True)
    x2 = models.FloatField(null=True, blank=True)
    x3 = models.FloatField(null=True, blank=True)
    x4 = models.FloatField(null=True, blank=True)
    x5 = models.FloatField(null=True, blank=True)
    x6 = models.FloatField(null=True, blank=True)
    x7 = models.FloatField(null=True, blank=True)
    x8 = models.FloatField(null=True, blank=True)
    x9 = models.FloatField(null=True, blank=True)
    x10 = models.FloatField(null=True, blank=True)
    x11 = models.FloatField(null=True, blank=True)
    x12 = models.FloatField(null=True, blank=True)
    x13 = models.FloatField(null=True, blank=True)
    x14 = models.FloatField(null=True, blank=True)
    x15 = models.FloatField(null=True, blank=True)
    x16 = models.FloatField(null=True, blank=True)
    x17 = models.FloatField(null=True, blank=True)
    x18 = models.FloatField(null=True, blank=True)
    x19 = models.FloatField(null=True, blank=True)
    x20 = models.FloatField(null=True, blank=True)
    x21 = models.FloatField(null=True, blank=True)
    x22 = models.FloatField(null=True, blank=True)
    x23 = models.FloatField(null=True, blank=True)
    x24 = models.FloatField(null=True, blank=True)
    x25 = models.FloatField(null=True, blank=True)
    x26 = models.FloatField(null=True, blank=True)
    x27 = models.FloatField(null=True, blank=True)
    x28 = models.FloatField(null=True, blank=True)
    x29 = models.FloatField(null=True, blank=True)
    x30 = models.FloatField(null=True, blank=True)
    x31 = models.FloatField(null=True, blank=True)
    x32 = models.FloatField(null=True, blank=True)
    x33 = models.FloatField(null=True, blank=True)
    x34 = models.FloatField(null=True, blank=True)
    x35 = models.FloatField(null=True, blank=True)
    x36 = models.FloatField(null=True, blank=True)
    x37 = models.FloatField(null=True, blank=True)
    x38 = models.FloatField(null=True, blank=True)
    x39 = models.FloatField(null=True, blank=True)
    x40 = models.FloatField(null=True, blank=True)
    x41 = models.FloatField(null=True, blank=True)
    x42 = models.FloatField(null=True, blank=True)
    x43 = models.FloatField(null=True, blank=True)
    x44 = models.FloatField(null=True, blank=True)
    x45 = models.FloatField(null=True, blank=True)
    x46 = models.FloatField(null=True, blank=True)
    x47 = models.FloatField(null=True, blank=True)
    x48 = models.FloatField(null=True, blank=True)
    x49 = models.FloatField(null=True, blank=True)
    x50 = models.FloatField(null=True, blank=True)
    x51 = models.FloatField(null=True, blank=True)
    x52 = models.FloatField(null=True, blank=True)
    x53 = models.FloatField(null=True, blank=True)
    x54 = models.FloatField(null=True, blank=True)
    x55 = models.FloatField(null=True, blank=True)
    x56 = models.FloatField(null=True, blank=True)
    x57 = models.FloatField(null=True, blank=True)
    x58 = models.FloatField(null=True, blank=True)
    x59 = models.FloatField(null=True, blank=True)
    x60 = models.FloatField(null=True, blank=True)
    x61 = models.FloatField(null=True, blank=True)
    x62 = models.FloatField(null=True, blank=True)
    x63 = models.FloatField(null=True, blank=True)
    x64 = models.FloatField(null=True, blank=True)
    x65 = models.FloatField(null=True, blank=True)
    x66 = models.FloatField(null=True, blank=True)
    x67 = models.FloatField(null=True, blank=True)
    x68 = models.FloatField(null=True, blank=True)
    x69 = models.FloatField(null=True, blank=True)
    x70 = models.FloatField(null=True, blank=True)
    x71 = models.FloatField(null=True, blank=True)
    x72 = models.FloatField(null=True, blank=True)
    x73 = models.FloatField(null=True, blank=True)
    x74 = models.FloatField(null=True, blank=True)
    x75 = models.FloatField(null=True, blank=True)
    x76 = models.FloatField(null=True, blank=True)
    x77 = models.FloatField(null=True, blank=True)
    x78 = models.FloatField(null=True, blank=True)
    x79 = models.FloatField(null=True, blank=True)
    x80 = models.FloatField(null=True, blank=True)
    x81 = models.FloatField(null=True, blank=True)
    x82 = models.FloatField(null=True, blank=True)
    x83 = models.FloatField(null=True, blank=True)
    x84 = models.FloatField(null=True, blank=True)
    x85 = models.FloatField(null=True, blank=True)
    x86 = models.FloatField(null=True, blank=True)
    x87 = models.FloatField(null=True, blank=True)
    x88 = models.FloatField(null=True, blank=True)
    x89 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return F"{self.clas.name}  {self.id}"



class Simptokompleks(models.Model):
    file = models.FileField(upload_to='simptokomplex', null=True)
    x1 = models.FloatField(null=True, blank=True)
    x2 = models.FloatField(null=True, blank=True)
    x3 = models.FloatField(null=True, blank=True)
    x4 = models.FloatField(null=True, blank=True)
    x5 = models.FloatField(null=True, blank=True)
    x6 = models.FloatField(null=True, blank=True)
    x7 = models.FloatField(null=True, blank=True)
    x8 = models.FloatField(null=True, blank=True)
    x9 = models.FloatField(null=True, blank=True)
    x10 = models.FloatField(null=True, blank=True)
    x11 = models.FloatField(null=True, blank=True)
    x12 = models.FloatField(null=True, blank=True)
    x13 = models.FloatField(null=True, blank=True)
    x14 = models.FloatField(null=True, blank=True)
    x15 = models.FloatField(null=True, blank=True)
    x16 = models.FloatField(null=True, blank=True)
    x17 = models.FloatField(null=True, blank=True)
    x18 = models.FloatField(null=True, blank=True)
    x19 = models.FloatField(null=True, blank=True)
    x20 = models.FloatField(null=True, blank=True)
    x21 = models.FloatField(null=True, blank=True)
    x22 = models.FloatField(null=True, blank=True)
    x23 = models.FloatField(null=True, blank=True)
    x24 = models.FloatField(null=True, blank=True)
    x25 = models.FloatField(null=True, blank=True)
    x26 = models.FloatField(null=True, blank=True)
    x27 = models.FloatField(null=True, blank=True)
    x28 = models.FloatField(null=True, blank=True)
    x29 = models.FloatField(null=True, blank=True)
    x30 = models.FloatField(null=True, blank=True)
    x31 = models.FloatField(null=True, blank=True)
    x32 = models.FloatField(null=True, blank=True)
    x33 = models.FloatField(null=True, blank=True)
    x34 = models.FloatField(null=True, blank=True)
    x35 = models.FloatField(null=True, blank=True)
    x36 = models.FloatField(null=True, blank=True)
    x37 = models.FloatField(null=True, blank=True)
    x38 = models.FloatField(null=True, blank=True)
    x39 = models.FloatField(null=True, blank=True)
    x40 = models.FloatField(null=True, blank=True)
    x41 = models.FloatField(null=True, blank=True)
    x42 = models.FloatField(null=True, blank=True)
    x43 = models.FloatField(null=True, blank=True)
    x44 = models.FloatField(null=True, blank=True)
    x45 = models.FloatField(null=True, blank=True)
    x46 = models.FloatField(null=True, blank=True)
    x47 = models.FloatField(null=True, blank=True)
    x48 = models.FloatField(null=True, blank=True)
    x49 = models.FloatField(null=True, blank=True)
    x50 = models.FloatField(null=True, blank=True)
    x51 = models.FloatField(null=True, blank=True)
    x52 = models.FloatField(null=True, blank=True)
    x53 = models.FloatField(null=True, blank=True)
    x54 = models.FloatField(null=True, blank=True)
    x55 = models.FloatField(null=True, blank=True)
    x56 = models.FloatField(null=True, blank=True)
    x57 = models.FloatField(null=True, blank=True)
    x58 = models.FloatField(null=True, blank=True)
    x59 = models.FloatField(null=True, blank=True)
    x60 = models.FloatField(null=True, blank=True)
    x61 = models.FloatField(null=True, blank=True)
    x62 = models.FloatField(null=True, blank=True)
    x63 = models.FloatField(null=True, blank=True)
    x64 = models.FloatField(null=True, blank=True)
    x65 = models.FloatField(null=True, blank=True)
    x66 = models.FloatField(null=True, blank=True)
    x67 = models.FloatField(null=True, blank=True)
    x68 = models.FloatField(null=True, blank=True)
    x69 = models.FloatField(null=True, blank=True)
    x70 = models.FloatField(null=True, blank=True)
    x71 = models.FloatField(null=True, blank=True)
    x72 = models.FloatField(null=True, blank=True)
    x73 = models.FloatField(null=True, blank=True)
    x74 = models.FloatField(null=True, blank=True)
    x75 = models.FloatField(null=True, blank=True)
    x76 = models.FloatField(null=True, blank=True)
    x77 = models.FloatField(null=True, blank=True)
    x78 = models.FloatField(null=True, blank=True)
    x79 = models.FloatField(null=True, blank=True)
    x80 = models.FloatField(null=True, blank=True)
    x81 = models.FloatField(null=True, blank=True)
    x82 = models.FloatField(null=True, blank=True)
    x83 = models.FloatField(null=True, blank=True)
    x84 = models.FloatField(null=True, blank=True)
    x85 = models.FloatField(null=True, blank=True)
    x86 = models.FloatField(null=True, blank=True)
    x87 = models.FloatField(null=True, blank=True)
    x88 = models.FloatField(null=True, blank=True)
    x89 = models.FloatField(null=True, blank=True)

class Tashxislassh(models.Model):
    etalon = models.ForeignKey(Etalon, on_delete=models.CASCADE, null=True, blank=True)
    middle_object = models.FloatField(null=True, blank=True)
    a = models.FloatField(null=True, blank=True, default=0)
    b = models.FloatField(null=True, blank=True)



class Patient(models.Model):
    normallash = models.ForeignKey(Normallash, on_delete=models.SET_NULL, null=True, blank=True)
    pat_doctor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    nolbir  = models.ForeignKey(Nolbir, on_delete=models.SET_NULL, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=125, null=True, blank=True)
    middle_name = models.CharField(max_length=125, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    home_phone = models.CharField(max_length=25, null=True, blank=True)
    work_phone = models.CharField(max_length=25, null=True, blank=True)
    region = models.CharField(max_length=125, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    gen = models.CharField(max_length=25, null=True, blank=True)
    work_place = models.CharField(max_length=125, null=True, blank=True)
    created_data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=35, null=True, blank=True)
    program_diagnos = models.CharField(max_length=255, null=True, blank=True)
    doctor_diagnos = models.CharField(max_length=255, null=True, blank=True)
    doctor = models.CharField(max_length=225, null=True, blank=True)
    partboss = models.CharField(max_length=225, null=True, blank=True)
    maindoctor = models.CharField(max_length=225, null=True, blank=True)
    document = models.FileField(upload_to='docx', null=True, blank=True)
    x1 = models.FloatField(null=True, blank=True)
    x2 = models.FloatField(null=True, blank=True)
    x3 = models.FloatField(null=True, blank=True)
    x4 = models.FloatField(null=True, blank=True)
    x5 = models.FloatField(null=True, blank=True)
    x6 = models.FloatField(null=True, blank=True)
    x7 = models.FloatField(null=True, blank=True)
    x8 = models.FloatField(null=True, blank=True)
    x9 = models.FloatField(null=True, blank=True)
    x10 = models.FloatField(null=True, blank=True)
    x11 = models.FloatField(null=True, blank=True)
    x12 = models.FloatField(null=True, blank=True)
    x13 = models.FloatField(null=True, blank=True)
    x14 = models.FloatField(null=True, blank=True)
    x15 = models.FloatField(null=True, blank=True)
    x16 = models.FloatField(null=True, blank=True)
    x17 = models.FloatField(null=True, blank=True)
    x18 = models.FloatField(null=True, blank=True)
    x19 = models.FloatField(null=True, blank=True)
    x20 = models.FloatField(null=True, blank=True)
    x21 = models.FloatField(null=True, blank=True)
    x22 = models.FloatField(null=True, blank=True)
    x23 = models.FloatField(null=True, blank=True)
    x24 = models.FloatField(null=True, blank=True)
    x25 = models.FloatField(null=True, blank=True)
    x26 = models.FloatField(null=True, blank=True)
    x27 = models.FloatField(null=True, blank=True)
    x28 = models.FloatField(null=True, blank=True)
    x29 = models.FloatField(null=True, blank=True)
    x30 = models.FloatField(null=True, blank=True)
    x31 = models.FloatField(null=True, blank=True)
    x32 = models.FloatField(null=True, blank=True)
    x33 = models.FloatField(null=True, blank=True)
    x34 = models.FloatField(null=True, blank=True)
    x35 = models.FloatField(null=True, blank=True)
    x36 = models.FloatField(null=True, blank=True)
    x37 = models.FloatField(null=True, blank=True)
    x38 = models.FloatField(null=True, blank=True)
    x39 = models.FloatField(null=True, blank=True)
    x40 = models.FloatField(null=True, blank=True)
    x41 = models.FloatField(null=True, blank=True)
    x42 = models.FloatField(null=True, blank=True)
    x43 = models.FloatField(null=True, blank=True)
    x44 = models.FloatField(null=True, blank=True)
    x45 = models.FloatField(null=True, blank=True)
    x46 = models.FloatField(null=True, blank=True)
    x47 = models.FloatField(null=True, blank=True)
    x48 = models.FloatField(null=True, blank=True)
    x49 = models.FloatField(null=True, blank=True)
    x50 = models.FloatField(null=True, blank=True)
    x51 = models.FloatField(null=True, blank=True)
    x52 = models.FloatField(null=True, blank=True)
    x53 = models.FloatField(null=True, blank=True)
    x54 = models.FloatField(null=True, blank=True)
    x55 = models.FloatField(null=True, blank=True)
    x56 = models.FloatField(null=True, blank=True)
    x57 = models.FloatField(null=True, blank=True)
    x58 = models.FloatField(null=True, blank=True)
    x59 = models.FloatField(null=True, blank=True)
    x60 = models.FloatField(null=True, blank=True)
    x61 = models.FloatField(null=True, blank=True)
    x62 = models.FloatField(null=True, blank=True)
    x63 = models.FloatField(null=True, blank=True)
    x64 = models.FloatField(null=True, blank=True)
    x65 = models.FloatField(null=True, blank=True)
    x66 = models.FloatField(null=True, blank=True)
    x67 = models.FloatField(null=True, blank=True)
    x68 = models.FloatField(null=True, blank=True)
    x69 = models.FloatField(null=True, blank=True)
    x70 = models.FloatField(null=True, blank=True)
    x71 = models.FloatField(null=True, blank=True)
    x72 = models.FloatField(null=True, blank=True)
    x73 = models.FloatField(null=True, blank=True)
    x74 = models.FloatField(null=True, blank=True)
    x75 = models.FloatField(null=True, blank=True)
    x76 = models.FloatField(null=True, blank=True)
    x77 = models.FloatField(null=True, blank=True)
    x78 = models.FloatField(null=True, blank=True)
    x79 = models.FloatField(null=True, blank=True)
    x80 = models.FloatField(null=True, blank=True)
    x81 = models.FloatField(null=True, blank=True)
    x82 = models.FloatField(null=True, blank=True)
    x83 = models.FloatField(null=True, blank=True)
    x84 = models.FloatField(null=True, blank=True)
    x85 = models.FloatField(null=True, blank=True)
    x86 = models.FloatField(null=True, blank=True)
    x87 = models.FloatField(null=True, blank=True)
    x88 = models.FloatField(null=True, blank=True)
    x89 = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"{self.last_name}   {self.first_name} {self.status}"

class Clas_ill_names(models.Model):
    clas = models.ForeignKey(Clas, models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=125, null=True, blank=True)

    def __str__(self):
        return self.clas.name


class Patient_informs(models.Model):
    calculus_status = models.BooleanField(null=True, blank=True, default=True)
    x1 = models.CharField(max_length=225, null=True, blank=True)
    x2 = models.CharField(max_length=225, null=True, blank=True)
    x3 = models.CharField(max_length=225, null=True, blank=True)
    x4 = models.CharField(max_length=225, null=True, blank=True)
    x5 = models.CharField(max_length=225, null=True, blank=True)
    x6 = models.CharField(max_length=225, null=True, blank=True)
    x7 = models.CharField(max_length=225, null=True, blank=True)
    x8 = models.CharField(max_length=225, null=True, blank=True)
    x9 = models.CharField(max_length=225, null=True, blank=True)
    x10 = models.CharField(max_length=225, null=True, blank=True)
    x11 = models.CharField(max_length=225, null=True, blank=True)
    x12 = models.CharField(max_length=225, null=True, blank=True)
    x13 = models.CharField(max_length=225, null=True, blank=True)
    x14 = models.CharField(max_length=225, null=True, blank=True)
    x15 = models.CharField(max_length=225, null=True, blank=True)
    x16 = models.CharField(max_length=225, null=True, blank=True)
    x17 = models.CharField(max_length=225, null=True, blank=True)
    x18 = models.CharField(max_length=225, null=True, blank=True)
    x19 = models.CharField(max_length=225, null=True, blank=True)
    x20 = models.CharField(max_length=225, null=True, blank=True)
    x21 = models.CharField(max_length=225, null=True, blank=True)
    x22 = models.CharField(max_length=225, null=True, blank=True)
    x23 = models.CharField(max_length=225, null=True, blank=True)
    x24 = models.CharField(max_length=225, null=True, blank=True)
    x25 = models.CharField(max_length=225, null=True, blank=True)
    x26 = models.CharField(max_length=225, null=True, blank=True)
    x27 = models.CharField(max_length=225, null=True, blank=True)
    x28 = models.CharField(max_length=225, null=True, blank=True)
    x29 = models.CharField(max_length=225, null=True, blank=True)
    x30 = models.CharField(max_length=225, null=True, blank=True)
    x31 = models.CharField(max_length=225, null=True, blank=True)
    x32 = models.CharField(max_length=225, null=True, blank=True)
    x33 = models.CharField(max_length=225, null=True, blank=True)
    x34 = models.CharField(max_length=225, null=True, blank=True)
    x35 = models.CharField(max_length=225, null=True, blank=True)
    x36 = models.CharField(max_length=225, null=True, blank=True)
    x37 = models.CharField(max_length=225, null=True, blank=True)
    x38 = models.CharField(max_length=225, null=True, blank=True)
    x39 = models.CharField(max_length=225, null=True, blank=True)
    x40 = models.CharField(max_length=225, null=True, blank=True)
    x41 = models.CharField(max_length=225, null=True, blank=True)
    x42 = models.CharField(max_length=225, null=True, blank=True)
    x43 = models.CharField(max_length=225, null=True, blank=True)
    x44 = models.CharField(max_length=225, null=True, blank=True)
    x45 = models.CharField(max_length=225, null=True, blank=True)
    x46 = models.CharField(max_length=225, null=True, blank=True)
    x47 = models.CharField(max_length=225, null=True, blank=True)
    x48 = models.CharField(max_length=225, null=True, blank=True)
    x49 = models.CharField(max_length=225, null=True, blank=True)
    x50 = models.CharField(max_length=225, null=True, blank=True)
    x51 = models.CharField(max_length=225, null=True, blank=True)
    x52 = models.CharField(max_length=225, null=True, blank=True)
    x53 = models.CharField(max_length=225, null=True, blank=True)
    x54 = models.CharField(max_length=225, null=True, blank=True)
    x55 = models.CharField(max_length=225, null=True, blank=True)
    x56 = models.CharField(max_length=225, null=True, blank=True)
    x57 = models.CharField(max_length=225, null=True, blank=True)
    x58 = models.CharField(max_length=225, null=True, blank=True)
    x59 = models.CharField(max_length=225, null=True, blank=True)
    x60 = models.CharField(max_length=225, null=True, blank=True)
    x61 = models.CharField(max_length=225, null=True, blank=True)
    x62 = models.CharField(max_length=225, null=True, blank=True)
    x63 = models.CharField(max_length=225, null=True, blank=True)
    x64 = models.CharField(max_length=225, null=True, blank=True)
    x65 = models.CharField(max_length=225, null=True, blank=True)
    x66 = models.CharField(max_length=225, null=True, blank=True)
    x67 = models.CharField(max_length=225, null=True, blank=True)
    x68 = models.CharField(max_length=225, null=True, blank=True)
    x69 = models.CharField(max_length=225, null=True, blank=True)
    x70 = models.CharField(max_length=225, null=True, blank=True)
    x71 = models.CharField(max_length=225, null=True, blank=True)
    x72 = models.CharField(max_length=225, null=True, blank=True)
    x73 = models.CharField(max_length=225, null=True, blank=True)
    x74 = models.CharField(max_length=225, null=True, blank=True)
    x75 = models.CharField(max_length=225, null=True, blank=True)
    x76 = models.CharField(max_length=225, null=True, blank=True)
    x77 = models.CharField(max_length=225, null=True, blank=True)
    x78 = models.CharField(max_length=225, null=True, blank=True)
    x79 = models.CharField(max_length=225, null=True, blank=True)
    x80 = models.CharField(max_length=225, null=True, blank=True)
    x81 = models.CharField(max_length=225, null=True, blank=True)
    x82 = models.CharField(max_length=225, null=True, blank=True)
    x83 = models.CharField(max_length=225, null=True, blank=True)
    x84 = models.CharField(max_length=225, null=True, blank=True)
    x85 = models.CharField(max_length=225, null=True, blank=True)
    x86 = models.CharField(max_length=225, null=True, blank=True)
    x87 = models.CharField(max_length=225, null=True, blank=True)
    x88 = models.CharField(max_length=225, null=True, blank=True)
    x89 = models.CharField(max_length=225, null=True, blank=True)



