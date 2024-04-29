from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


NUCLEOTYDE = [
    ('A', 'A'),
    ('T', 'T'),
    ('C', 'C'),
    ('G', 'G'),
]


class Animal(models.Model):
    name = models.CharField(max_length=128)
    latin_name = models.CharField(max_length=256)
    chromosome_count = models.IntegerField()
    image = models.ImageField()


class Chromosome(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    number = models.IntegerField()


class SNP(models.Model):
    chromosome = models.ForeignKey(Chromosome, on_delete=models.CASCADE)
    position = models.IntegerField()
    ref_allele = models.CharField(max_length=1, choices=NUCLEOTYDE)
    alt_allele = models.CharField(max_length=1, choices=NUCLEOTYDE)
    maf = models.DecimalField(max_digits=4, decimal_places=3)


class Annotation(models.Model):
    snp = models.ForeignKey(SNP, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

