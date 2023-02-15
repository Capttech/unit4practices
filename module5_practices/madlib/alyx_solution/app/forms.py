from django import forms


class MadlibForm(forms.Form):
    date = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    noun = forms.CharField(max_length=200)
    adjective = forms.CharField(max_length=200)
    signed_by = forms.CharField(max_length=200)
