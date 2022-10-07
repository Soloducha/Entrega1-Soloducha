from django.contrib import admin
from django.urls import path

from Veterinaria.views import (
    buscar_cliente,
    buscar_animal,
    buscar_veterinario,
    inicio,
    procesar_formulario_cliente,
    procesar_formulario_animal,
    procesar_formulario_veterinario,

)


urlpatterns = [
    path("", inicio),
    path("formulario_cliente/", procesar_formulario_cliente),
    path("formulario_animal/", procesar_formulario_animal),
    path("formulario_veterinario/", procesar_formulario_veterinario),
    path("buscar_cliente/", buscar_cliente),
    path("buscar_animal/", buscar_animal),
    path("buscar_veterinario/", buscar_veterinario),

]      