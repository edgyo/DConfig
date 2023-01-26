from django.contrib import admin
from .models import CPU, GPU, RAM, Case, SSD, HDD, Configuration, Motherboard, PowerSupply

# Register your models here.
admin.site.register(Motherboard)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(Case)
admin.site.register(SSD)
admin.site.register(HDD)
admin.site.register(PowerSupply)
admin.site.register(Configuration)