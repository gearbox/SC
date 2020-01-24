from django.db import models
from django.utils import timezone
# Create your models here.


class Language(models.Model):
    alpha_3 = models.CharField(verbose_name='Short language name', max_length=3, unique=True, null=True)  # , blank=True, null=True
    name = models.CharField(verbose_name='Language name', max_length=30, blank=True)  # , default='English'
    country = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.alpha_3 + ' (' + self.name + ')'


class Message(models.Model):
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    voice_message_text = models.CharField(max_length=200)
    audio_file_name = models.CharField(max_length=30, blank=True)
    image_file_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.voice_message_text


class Type(models.Model):
    name = models.CharField(verbose_name='SpeedCam code name', max_length=100, unique=True)
    number = models.PositiveSmallIntegerField(verbose_name='SpeedCam type number', unique=True)
    description = models.TextField(verbose_name='SpeedCam description', max_length=200, blank=True)
    message = models.ForeignKey(to=Message, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return 'Type: ' + str(self.number) + '; ' + self.description


class Method(models.Model):
    name = models.CharField(verbose_name='Method name', max_length=30, unique=True, default=False)

    def __str__(self):
        return self.name


class SCPoint(models.Model):
    lon = models.DecimalField(verbose_name='Longitude (X)', max_digits=11, decimal_places=8)  # , default=0
    lat = models.DecimalField(verbose_name='Latitude (Y)', max_digits=11, decimal_places=8)
    type = models.ForeignKey(verbose_name='SpeedCam Type', to=Type, on_delete=models.CASCADE)
    speed = models.PositiveSmallIntegerField(verbose_name='Speed limit', default=0)
    dirtype = models.PositiveSmallIntegerField(default=1)
    direction = models.SmallIntegerField(verbose_name='Direction from which SC catches', default=0)
    method = models.ForeignKey(verbose_name='Method name', to=Method, on_delete=models.CASCADE, blank=True)
    danger = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(default=0)
    add_date = models.DateTimeField(verbose_name='Date on which the SpeedCam was added', default=timezone.now)
    active = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    def __str__(self):
        return 'ID: ' + str(self.id) + '; Type: ' + str(self.type.number) + '; ' + self.type.description
