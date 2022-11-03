from django import forms

class ContactUsForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=10)