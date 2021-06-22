from django.shortcuts import render

# Create your views here.

def Inicio(request):

    return render(request, 'AppWeb/Inicio.html')

def Tienda(request):

    return render(request, 'AppWeb/Tienda.html')

def Servicios(request):

    return render(request, 'AppWeb/Servicios.html')

def Contactanos(request):

    return render(request, 'AppWeb/Contactanos.html')

