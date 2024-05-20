from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import SNPForm
from .models import Animal, SNP

def index(request):
    species = Animal.objects.all().count()
    snps = SNP.objects.all().count()
    return render(
        request,
        "snp/index.html",
        {
            "species": species,
            "snps": snps, 
        }
    )


def search(request):
    animal_id = -1
    animals = Animal.objects.all()
    snps = []
    if request.method == "POST":
        form = SNPForm(request.POST)
        if form.is_valid():
            animal_id = form.cleaned_data["animal"]
            animal = get_object_or_404(Animal, pk=animal_id)

            region_str = form.cleaned_data["region"]
            chromosome, rangestr = region_str.split(':')
            range_min, range_max = rangestr.split('-')

            chromosome = int(chromosome)
            range_min = int(range_min)
            range_max = int(range_max)

            maf_min = form.cleaned_data["maf_min"]
            maf_max = form.cleaned_data["maf_max"]

            snps = SNP.objects.filter(
                chromosome__animal=animal,
                chromosome__number=chromosome,
                maf__gte=maf_min, maf__lte=maf_max
            )
    else:
        form = SNPForm()
    

    return render(
        request,
        "snp/search.html",
        {
            "animal_id": animal_id,
            "animals": animals,
            "form": form,
            "snps": snps,
        }
    )