from django import forms


class RequestForm(forms.Form):
    method = forms.CharField()
    url = forms.CharField()