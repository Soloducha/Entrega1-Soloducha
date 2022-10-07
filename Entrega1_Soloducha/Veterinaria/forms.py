from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=20)


class VeterinarioForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    matricula = forms.IntegerField()


class AnimalForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    dueño_nombre = forms.CharField(max_length=40)
    dueño_apellido = forms.CharField(max_length=40)
    raza = forms.CharField(max_length=20)