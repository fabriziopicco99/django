from django.shortcuts import render, redirect
from .form import (
    AutoForm,
    PersonaForm,
    AnimalesForm,
    AutoBuscar,
    PersonaBuscar,
    AnimalBuscar,
)
from .models import Autos, Persona, Animal


# Create your views here.
def home(request):
    return render(request, "home.html")


def getAutos(request):
    params = {}
    año = request.GET.get("año")
    marca = request.GET.get("marca")
    modelo = request.GET.get("modelo")
    precio = request.GET.get("precio")
        
    # Agregamos los parametros de busqueda al diccionario
    if año:
        params["año"] = año
    if marca:
        params["marca"] = marca
    if modelo:
        params["modelo"] = modelo
    if precio:
        params["precio"] = precio
    
    # Obtenemos todos los registros de la tabla
    # Si no hay parametros de busqueda traer todos los registros
    if params == {}:
        autos = Autos.objects.all()
    else:
        # Filtramos los registros de la tabla que cumplan con los parametros de busqueda
        autos = Autos.objects.filter(**params)
    
    # Creamos un diccionario con los datos que se van a enviar a la vista
    data = {"form": AutoForm(), "form_buscar": AutoBuscar(), "autos": autos}

    return render(request, "autos.html", data)

def agregarAuto(request):
    print(request.POST)
    #Obtenemos los parametros del formulario para despues crear un nuevo registro
    params = {"año": int(request.POST["año"]), "marca": request.POST["marca"], "modelo": request.POST["modelo"], "precio":request.POST["precio"]}
    print(params)
    #Creamos un nuevo registro en la tabla
    Autos.objects.create(**params)
    #Redireccionamos a la vista de autos
    return redirect('/autos')


def getPersonas(request):
    params = {}
    nombre = request.GET.get("nombre")
    edad = request.GET.get("edad")
    servicio = request.GET.get("servicio")
    apellido = request.GET.get("apellido")
        
    #Agregamos los parametros de busqueda al diccionario
    if nombre:
        params["nombre"] = nombre
    if edad:
        params["edad"] = edad
    if servicio:
        params["servicio"] = servicio
    if apellido:
        params["apellido"] = apellido
    
    #Obtenemos todos los registros de la tabla
    #Si no hay parametros de busqueda traer todos los registros
    if params == {}:
        personas = Persona.objects.all()
    else:
        #filtramos los registros de la tabla que cumplan con los parametros de busqueda
        personas = Persona.objects.filter(**params)
    
    #Creamos un diccionario con los datos que se van a enviar a la vista
    data = {"form": PersonaForm(), "form_buscar": PersonaBuscar(), "personas": personas}

    return render(request, "personas.html",data)

def agregarPersona(request):
    #Obtenemos los parametros del formulario para despues crear un nuevo registro
    params = {"nombre": request.POST["nombre"], "edad": request.POST["edad"], "servicio": request.POST["servicio"], "apellido": request.POST["apellido"]}
    #Creamos un nuevo registro en la tabla
    Persona.objects.create(nombre=params["nombre"], edad=params["edad"], servicio=params["servicio"], apellido=params["apellido"])
    #Redireccionamos a la vista de personas
    return redirect('/personas')


def getAnimales(request):
    #Obtenemos los parametros de busqueda
    params = {}
    nombre = request.GET.get("nombre")
    especie = request.GET.get("especie")
    #Agregamos los parametros de busqueda al diccionario
    if nombre:
        params["nombre"] = nombre
    if especie:
        params["especie"] = especie
    
    #Obtenemos todos los registros de la tabla
    #Si no hay parametros de busqueda traer todos los registros
    if params == {}:
        animales = Animal.objects.all()
    else:
        #filtramos los registros de la tabla que cumplan con los parametros de busqueda
        animales = Animal.objects.filter(**params)
    
    #Creamos un diccionario con los datos que se van a enviar a la vista
    data = {"form": AnimalesForm(), "form_buscar": AnimalBuscar(), "animales": animales}

    return render(request, "animales.html", data)


def agregarAnimales(request):
    #Obtenemos los parametros del formulario para despues crear un nuevo registro
    params = {"nombre": request.POST["nombre"], "especie": request.POST["especie"]}
    #Creamos un nuevo registro en la tabla
    Animal.objects.create(nombre=params["nombre"], especie=params["especie"])
    #Redireccionamos a la vista de animales
    return redirect('/animales')
