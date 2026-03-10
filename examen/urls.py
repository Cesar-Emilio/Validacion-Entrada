from django.urls import path

from ejercicio import views as ejercicio

urlpatterns = [
    path('formulario/', ejercicio.formulario_view, name='formulario'),
    path('scroll/', ejercicio.scroll_view, name='scroll'),
]
