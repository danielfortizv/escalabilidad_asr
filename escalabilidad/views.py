from django.shortcuts import render

def index(request):
    return render(request, 'escalabilidad/index.html')

def escalabilidad_view(request):
    context = {
        'examenes': ['MRI 1', 'MRI 2', 'MRI 3', 'MRI 4', 'MRI 5', 'MRI 6']
    }
    return render(request, 'escalabilidad/escalabilidad.html', context)
