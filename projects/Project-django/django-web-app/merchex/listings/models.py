from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        INDIE_ROCK = 'IR'
        POP = 'PO'
        JAZZ = 'JA'
        BLUES = 'BL'
        COUNTRY = 'CO'
        ELECTRONIC = 'EL'
        TECHNO = 'TE'
        CLASSICAL = 'CL'
        REGGAE = 'RE'
        METAL = 'ME'
        PUNK = 'PU'
        FUNK = 'FU'
        R_AND_B = 'RB'
        SOUL = 'SO'
        FOLK = 'FO'
        WORLD = 'WO'
        OTHER = 'OT'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepag = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    class type(models.TextChoices):
        CD = 'CD'
        VINYL = 'VL'
        CASSETTE = 'CS'
        POSTER = 'PO'
        CLOTHING = 'CL'
        OTHER = 'OT'

    def __str__(self):
        return self.title
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
