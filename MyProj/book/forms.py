from django import forms
from datetime import datetime

from book.models import Voo

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        exclude = ('partidaReal', 'chegadaReal', 'statusVoo')
        # fields = '__all__'
        # widgets = {'idVoo'}

    def clean_conexoes(self):
        rota = self.data.get('conexoes')
        origem = self.data.get('origem')
        destino = self.data.get('destino')
        if rota == '':
            rota = f'{origem} - {destino}'

        return rota

class VooStatusForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = ('statusVoo', 'partidaReal', 'chegadaReal')
        widgets = {'partidaReal': forms.HiddenInput(),
                   'chegadaReal': forms.HiddenInput()}

    def clean_statusVoo(self):
        currentStatus = self.instance.statusVoo
        statusVoo = self.data.get('statusVoo')
        statusOrder = {
            "Confirmado": 0,
            "Embarcando": 1,
            "Cancelado": 1,
            "Programado": 2,
            "Taxiando": 3,
            "Pronto": 4,
            "Autorizado": 5,
            "Em Voo": 6,
            "Aterrissado": 7
        }
        
        currentOrder = statusOrder[currentStatus]
        newOrder = statusOrder[statusVoo]
        print(currentOrder + newOrder)
        if newOrder < currentOrder or newOrder > currentOrder + 1:
            self.add_error('statusVoo', 'Transição de status inválida')

        return statusVoo

    def clean_partidaReal(self):
        statusVoo = self.data.get('statusVoo')
        partidaReal = self.data.get('partidaReal')
        if statusVoo == 'Autorizado' and partidaReal != None:
            return datetime.now()
        else:
            return partidaReal

    def clean_chegadaReal(self):
        statusVoo = self.data.get('statusVoo')
        chegadaReal = self.data.get('chegadaReal')
        if statusVoo == 'Aterrissado' and chegadaReal != None:
            return datetime.now()
        else:
            return chegadaReal



class DtIntervalForm(forms.Form):
    dtInicio = forms.DateTimeField()
    dtFim = forms.DateTimeField()