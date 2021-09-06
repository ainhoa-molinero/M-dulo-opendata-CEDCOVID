from django.urls import path, include
from . import views

urlpatterns = [
    path('l/<str:id_linea>', views.lineas, name ='lineas'),
    path('a/<str:id_archivo>', views.perfil_archivo, name ='perfil_archivo'),
    path('p/<str:id_producto>', views.perfil_producto, name ='perfil_producto'),
    path('listado_archivos/', views.lista_archivos, name ='lista_archivos'),
    path('listado_lineas/', views.lista_lineas, name ='lista_lineas'),
    path('datos_abiertos/', views.datos_abiertos, name ='datos_abiertos'),
    #path('listado/', views.categorias, name ='categorias'),
]
