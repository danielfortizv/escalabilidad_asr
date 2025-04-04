import io
import os  
import requests
import numpy as np
from PIL import Image
import nibabel as nib
from .utils import nifti_a_png  
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

BACKEND_URL = "http://34.117.229.99/services"

def index(request):
    return render(request, 'escalabilidad/index.html')

def escalabilidad_view(request):
    try:
        # Hacemos una petición GET al backend para obtener la lista de eventos
        response = requests.get(f"{BACKEND_URL}/eventos/")
        response.raise_for_status()
        eventos = response.json()
        error = None
    except requests.RequestException as e:
        eventos = []
        error = f"Error al conectar con el backend: {e}"
        print(error)
    
    context = {'eventos': eventos, 'error': error}
    return render(request, 'escalabilidad/escalabilidad.html', context)

def obtener_examenes_mri(request, td, cedula):
    try:
        response = requests.get(f"{BACKEND_URL}/mris/{td}/{cedula}")
        response.raise_for_status()
        examenes = response.json()
        error = None
    except requests.RequestException as e:
        examenes = []
        error = f"Error al conectar con el backend: {e}"
        print(error)
    
    return render(request, 'escalabilidad/examenes_mri.html', {'examenes': examenes, 'error': error})

def obtener_eventos(request):
    try:
        response = requests.get(f"{BACKEND_URL}/eventos/")
        response.raise_for_status()
        eventos = response.json()
    except requests.RequestException as e:
        eventos = []
        print(f"Error al conectar con el backend: {e}")
    
    return render(request, 'escalabilidad/eventos.html', {'eventos': eventos})

def detalle_examen_mri(request, sujeto_id):
    # Ruta completa del archivo MRI
    archivo_nifti = os.path.join(settings.MEDIA_ROOT, f'mri_data/sub-{sujeto_id}/anat/sub-{sujeto_id}_acq-iso08_T1w.nii.gz')
    
    # Cargar el archivo usando nibabel
    try:
        img = nib.load(archivo_nifti)
        data = img.get_fdata()
        
        # Vamos a tomar una sola capa de la imagen para mostrarla (por ejemplo, la mitad)
        slice_index = data.shape[2] // 2
        slice_data = data[:, :, slice_index]
        
        # Convertir la imagen a formato PIL
        slice_image = Image.fromarray(np.uint8(slice_data / np.max(slice_data) * 255))

        # Convertir la imagen a PNG y retornar en la respuesta HTTP
        response = HttpResponse(content_type="image/png")
        slice_image.save(response, "PNG")
        return response
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)