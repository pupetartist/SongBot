from django import forms

class FormularioBusquedaDeMusica(forms.Form):
    lyrics =  forms.CharField()
