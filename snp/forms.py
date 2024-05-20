from django import forms

from .models import Animal, SNP, Chromosome

class SNPForm(forms.Form):
    animal = forms.IntegerField(label="Animal", widget=forms.HiddenInput())
    region = forms.CharField(label="Region")
    maf_min = forms.FloatField(label="Min. value", min_value=0.0, max_value=0.5)
    maf_max = forms.FloatField(label="Max. value", min_value=0.0, max_value=0.5)