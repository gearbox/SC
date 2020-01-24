from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField()
    alpha_2 = models.CharField(max_length=2)
    alpha_3 = models.CharField(max_length=3)


class Country(models.Model):
    name = models.CharField(verbose_name='Name', max_length=30)
    fullname = models.CharField(verbose_name='Full name', max_length=200, blank=True)
    official_language = models.CharField(verbose_name='Official language', max_length=30)
    alpha_2 = models.CharField(verbose_name='2 letter code', max_length=2)
    alpha_3 = models.CharField(verbose_name='3 letter code', max_length=3)
    iso = models.PositiveSmallIntegerField(blank=True)
    location = models.CharField(verbose_name='Country location', max_length=30, blank=True)

    def __str__(self):
        return self.alpha_3 + '; ' + self.name
