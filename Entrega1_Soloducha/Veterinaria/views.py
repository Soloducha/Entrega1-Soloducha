from multiprocessing import context
from django.shortcuts import render
from Veterinaria.models import Cliente, Animal, Veterinario
from Veterinaria.forms import ClienteForm, AnimalForm, VeterinarioForm


def buscar_cliente(request):
    if request.method == "GET":
        return render(request, "Veterinaria/busqueda_de_cliente.html")

    if request.method == "POST":
        nombre_a_buscar = request.POST["nombre"] 
        resultados_de_busqueda = Cliente.objects.filter(nombre=nombre_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "Veterinaria/resultado_cliente.html", context=contexto)


def buscar_animal(request):
    if request.method == "GET":
        return render(request, "Veterinaria/busqueda_de_animal.html")

    if request.method == "POST":
        nombre_a_buscar = request.POST["nombre"]
        resultados_de_busqueda = Animal.objects.filter(nombre=nombre_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "Veterinaria/resultado_animal.html", context=contexto)


def buscar_veterinario(request):
    if request.method == "GET":
        return render(request, "Veterinaria/busqueda_de_veterinario.html")

    if request.method == "POST":
        matricula_a_buscar = request.POST["matricula"]
        resultados_de_busqueda = Veterinario.objects.filter(matricula=matricula_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "Veterinaria/resultado_veterinario.html", context=contexto)


def inicio(request):
    return render(request, "Veterinaria/inicio.html")


def procesar_formulario_cliente(request):
    if request.method == "GET":
        mi_formulario = ClienteForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Veterinaria/formulario_cliente.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ClienteForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Cliente(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                telefono=datos_ingresados_por_usuario["telefono"],
            )
            nuevo_modelo.save()

            return render(request, "Veterinaria/exito.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Veterinaria/formulario_cliente.html", context=contexto)


def procesar_formulario_animal(request):
    if request.method == "GET":
        mi_formulario = AnimalForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Veterinaria/formulario_animal.html", context=contexto)

    if request.method == "POST":

        mi_formulario = AnimalForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Animal(
                nombre=datos_ingresados_por_usuario["nombre"],
                dueño_nombre=datos_ingresados_por_usuario["dueño_nombre"],
                dueño_apellido=datos_ingresados_por_usuario["dueño_apellido"],
                raza=datos_ingresados_por_usuario["raza"],
            )
            nuevo_modelo.save()

            return render(request, "Veterinaria/exito.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Veterinaria/formulario_cliente.html", context=contexto)


def procesar_formulario_veterinario(request):
    if request.method == "GET":
        mi_formulario = VeterinarioForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Veterinaria/formulario_veterinario.html", context=contexto)

    if request.method == "POST":

        mi_formulario = VeterinarioForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Veterinario(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                matricula=datos_ingresados_por_usuario["matricula"],
            )
            nuevo_modelo.save()

            return render(request, "Veterinaria/exito.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "Veterinaria/formulario_veterinario.html", context=contexto)
