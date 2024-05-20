from django.contrib import admin

from .models import Animal, Chromosome, SNP


class ChromosomeInline(admin.TabularInline):
    model = Chromosome
    extra = 3


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Species", {"fields": ["name", "latin_name", "chromosome_count"]}),
        ("Presentation", {"fields": ["image"], "classes": ["collapse"]}),
    ]
    inlines = [ChromosomeInline]
    list_display = ["name", "latin_name"]
    search_fields = ["name", "latin_name"]


class SNPInline(admin.TabularInline):
    model = SNP
    extra = 1


@admin.register(Chromosome)
class ChromosomeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["animal", "number"]}),
    ]
    inlines = [SNPInline]
    list_display = ["animal"]