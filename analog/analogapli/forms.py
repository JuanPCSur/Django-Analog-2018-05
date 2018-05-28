from django import forms
# del docs django project.
class Analogform(forms.Form):
    intentos = forms.IntegerField(label='Inteentos')
    intervalo = forms.IntegerField(label = 'Intervalo')
