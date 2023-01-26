from ast import Pow
from sqlite3 import OperationalError
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect

from .models import *

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def config(request, id):
    Config = Configuration.objects.get(id = id)
    price = Config.Case.price + Config.CPU.price + Config.GPU.price + Config.RAM.price + Config.SSD.price + Config.HDD.price + Config.PowerSupply.price + Config.Motherboard.price
    context = {
        'Config': Config,
        'price' : price,
    }
    return render(request, "config.html", context)

def configs(request):
    try:
        CONFIG_list = Configuration.objects.all()
        for Config in CONFIG_list:
            Config.price = Config.Case.price + Config.CPU.price + Config.GPU.price + Config.RAM.price + Config.SSD.price + Config.HDD.price + Config.PowerSupply.price + Config.Motherboard.price
        context = {
        'CONFIG_list': CONFIG_list,
        }
    except OperationalError:
        return Http404("No items currently available")
    return render(request, "configs.html", context)

def components(request):
    try:
        CPU_list = CPU.objects.all()
        MB_list = Motherboard.objects.all()
        GPU_list = GPU.objects.all()
        RAM_list = RAM.objects.all()
        CASE_list = Case.objects.all()
        SSD_list = SSD.objects.all()
        HDD_list = HDD.objects.all()
        PS_list = PowerSupply.objects.all()
        context = {
        'CPU_list': CPU_list,
        'MB_list' : MB_list,
        'GPU_list' : GPU_list,
        'RAM_list' : RAM_list,
        'CASE_list' : CASE_list,
        'SSD_list' : SSD_list,
        'HDD_list' : HDD_list,
        'PS_list' : PS_list
    }
    except OperationalError:
        return Http404("No items currently available")
    return render(request, "components.html", context)
    
def configurator(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ConfigurationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            configuration = form.save()
            configuration.price = configuration.Case.price + configuration.CPU.price + configuration.GPU.price + configuration.RAM.price + configuration.SSD.price + configuration.HDD.price + configuration.PowerSupply.price + configuration.Motherboard.price
            return HttpResponseRedirect('/config/'+str(configuration.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConfigurationForm()

    context = {
        'form' : form
    }

    return render(request, "configurator.html", context)