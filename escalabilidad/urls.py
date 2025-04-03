from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('escalabilidad/', views.escalabilidad_view, name='escalabilidad'),
]
