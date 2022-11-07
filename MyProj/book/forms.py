from django import forms

from book.models import Voo

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = '__all__'
        # fields = ('idVoo', 'companhiaAerea', 'origem', 'destino', 'partidaPrevista', 'chegadaPrevista', 'conexoes')
        # widgets = {
        #     'idVoo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: PCS3643'}),
        #     'companhiaAerea' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Laboratório de Engenharia de Software I Airline'}),
        #     'origem' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Escola  Politécnica'}),
        #     'destino' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: Escola  Politécnica'}),
        #     'partidaPrevista' : forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': ''}),
        #     'chegadaPrevista' : forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': ''}),
        #     'conexoes' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''})
        # }