from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.core.files.uploadedfile import UploadedFile
from random import randrange, choice, uniform
from snp.models import Animal, Chromosome, SNP, Annotation


def create_annotations(snp):
    for i in range(randrange(5)):
        a = Annotation(snp=snp, text="Lorem ipsum", author=choice(User.objects.all()))
        a.save()


def create_snp(chromosome):
    s = SNP(chromosome=chromosome, position=randrange(1, 1000), 
    ref_allele=choice(['A', 'C', 'G', 'T']), alt_allele=choice(['A', 'C', 'G', 'T']),
    maf=uniform(0.0, 0.5))
    s.save()
    create_annotations(s)


def create_chromosomes(animal, i):
    ch = Chromosome(animal=animal, number=i)
    ch.save()
    for j in range(randrange(5, 20)):
        create_snp(ch)


def create_animals():
    animals = [
        {"name": "Daniel", "latin": "Dama dama", "image": "img/Dama_dama8.JPG"},
        {"name": "Jeleń", "latin": "Cervus elaphus", "image": "img/jelen.jpg"},
    ]
    for animal in animals:
        chromosomes = randrange(5, 45)
        a = Animal(name=animal["name"], latin_name=animal["latin"], 
                    image=UploadedFile(file=open(animal["image"], "rb")), chromosome_count=chromosomes)
        a.save()
        for i in range(chromosomes):
            create_chromosomes(a, i+1)


class Command(BaseCommand):
    help = "Creates dummy data to be used in database"

    # def add_arguments(self, parser):
        # parser.add_argument("animal_list")
        # parser.add_argument("animal_count", type=int)
        # parser.add_argument("chromosome_min_count", type=int)
        # parser.add_argument("chromosome_max_count", type=int)
        # parser.add_argument("snp_min_count", type=int)
        # parser.add_argument("snp_max_count", type=int)
        # parser.add_argument("annotation_min_count", type=int)
        # parser.add_argument("annotation_max_count", type=int)

    def handle(self, *args, **options):
        create_animals()
