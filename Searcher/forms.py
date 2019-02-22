from django import forms

class search(forms.Form):
    your_name = forms.CharField(label='Imagen a buscar:', max_length=100)