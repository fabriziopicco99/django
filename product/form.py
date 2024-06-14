from django import forms

#Formulario de animales
class AnimalBuscar(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=100, required=False)
    especie = forms.CharField(label="Especie",max_length=100, required=False)

class AnimalesForm(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=100, required=True)
    especie = forms.CharField(label="Especie",max_length=100, required=True)
    
#Formulario de personas
class PersonaBuscar(forms.Form):
    nombre = forms.CharField(label="Nombre",max_length=100, required=False)
    apellido = forms.CharField(label="Apellido",max_length=100, required=False)
    edad = forms.IntegerField(label="Edad", required=False)
    servicio = forms.CharField(label="Servicio",max_length=100,required=False)
    
class PersonaForm(forms.Form):
    nombre = forms.CharField(label= "Nombre",max_length=100,required=True)
    apellido = forms.CharField(label="Apellido",max_length=100, required=True)
    edad = forms.IntegerField(label="Edad",required=True)
    servicio = forms.CharField(label="Servicio",max_length=100,required=True)


#Formulario de autos
class AutoBuscar(forms.Form):
    marcar = forms.CharField(label="Marca",max_length=100, required=False)
    modelo = forms.CharField(label="Modelo",max_length=100, required=False)
    año = forms.DateField(label="Año", required=False)
    precio = forms.IntegerField(label="Precio", required=False)
    
class AutoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=100, required=True)
    modelo = forms.CharField(label="Modelo", max_length=100, required=True)
    año = forms.DateField(label="Año", required=True)
    precio = forms.IntegerField(label="Precio", required=True)
    