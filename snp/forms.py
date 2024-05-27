from django import forms

from .models import Animal, SNP, Chromosome


class SNPForm(forms.Form):
    animal = forms.IntegerField(label="Animal", widget=forms.HiddenInput(), initial=-1, min_value=0)
    region = forms.CharField(label="Region", initial=":0-1000")
    region.widget.attrs.update({"class": "form-control"})
    maf_min = forms.FloatField(label="Min. value", min_value=0.0, max_value=0.5, initial=0.0)
    maf_min.widget.attrs.update({"class": "form-control"})
    maf_max = forms.FloatField(label="Max. value", min_value=0.0, max_value=0.5, initial=0.5)
    maf_max.widget.attrs.update({"class": "form-control"})
