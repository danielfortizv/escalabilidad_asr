import requests
from django.shortcuts import render
from django.http import JsonResponse

BACKEND_URL = "http://34.117.229.99/services"

def index(request):
    return render(request, 'escalabilidad/index.html')

def escalabilidad_view(request):
    try:
        # Hacemos una petición GET al backend para obtener la lista de eventos
        response = requests.get(f"{BACKEND_URL}/eventos/")
        response.raise_for_status()  # Si hay un error en la respuesta, lanza una excepción
        eventos = response.json()  # Convertimos la respuesta en JSON
    except requests.RequestException as e:
        eventos = []
        print(f"Error al conectar con el backend: {e}")
    
    context = {'eventos': eventos}
    return render(request, 'escalabilidad/escalabilidad.html', context)

def obtener_eventos(request):
    try:
        response = requests.get(f"{BACKEND_URL}/eventos/")
        response.raise_for_status()
        eventos = response.json()
    except requests.RequestException as e:
        eventos = []
        print(f"Error al conectar con el backend: {e}")
    
    return render(request, 'escalabilidad/eventos.html', {'eventos': eventos})

def obtener_examenes_mri(request, td, cedula):
    try:
        response = requests.get(f"{BACKEND_URL}/mris/{td}/{cedula}")
        response.raise_for_status()
        examenes = response.json()
    except requests.RequestException as e:
        examenes = []
        print(f"Error al conectar con el backend: {e}")
    
    return render(request, 'escalabilidad/examenes_mri.html', {'examenes': examenes})