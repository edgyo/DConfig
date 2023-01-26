from ast import Pow
from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 120)
    price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to ='uploads/')
    
    def __str__(self):
        return(self.name)

class Motherboard(Product):
    SOCKET_CHOICES = (
        ('LGA12', 'LGA 1200'),
        ('LGA17', 'LGA 1700'),
        ('AM4', 'AM4')
    )
    socket = models.CharField(max_length=20, choices=SOCKET_CHOICES, default='LGA12')

class CPU(Product):
    SOCKET_CHOICES = (
        ('LGA12', 'LGA 1200'),
        ('LGA17', 'LGA 1700'),
        ('AM4', 'AM4')
    )
    socket = models.CharField(max_length=20, choices=SOCKET_CHOICES, default='LGA12')

class GPU(Product):
    pass

class RAM(Product):
    pass

class Case(Product):
    pass

class SSD(Product):
    pass

class HDD(Product):
    pass

class PowerSupply(Product):
    pass

class Configuration(models.Model):
    PURPOSE_CHOICES = (
    ('gaming', 'Игровая'),
    ('office', 'Для офиса'),
    ('home', 'Домашняя'),
    )

    name = models.CharField(max_length = 120)
    type = models.CharField(max_length = 120, choices = (('official', 'Официальная'), ('custom', 'Пользовательская')), default='custom')
    purpose = models.CharField(max_length = 120, choices = PURPOSE_CHOICES, default='home')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CPU = models.ForeignKey(CPU, on_delete=models.CASCADE, default=None)
    Motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE, default=None)
    GPU = models.ForeignKey(GPU, on_delete=models.CASCADE, default=None)
    RAM = models.ForeignKey(RAM, on_delete=models.CASCADE, default=None)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE, default=None)
    SSD = models.ForeignKey(SSD, on_delete=models.CASCADE, default=None)
    HDD = models.ForeignKey(HDD, on_delete=models.CASCADE, default=None)
    PowerSupply = models.ForeignKey(PowerSupply, on_delete=models.CASCADE, default=None)
    price = models.IntegerField(default=0)
    def __str__(self):
        return(self.name)

class ConfigurationForm(ModelForm):
    class Meta:
        model = Configuration
        fields = ['name', 'purpose', 'CPU', 'Motherboard', 'GPU', 'RAM', 'Case', 'SSD', 'HDD', 'PowerSupply']




