from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('escalabilidad/', views.escalabilidad_view, name='escalabilidad'),
    path('eventos/', views.obtener_eventos, name='obtener_eventos'),
    path('mris/<str:td>/<str:cedula>/', views.obtener_examenes_mri, name='obtener_examenes_mri'),
    path('examen_mri/<str:sujeto_id>/', views.detalle_examen_mri, name='detalle_examen_mri'),
]