from django.db import models

# Create your models here.


class Message(models.Model):
    language = models.CharField(max_length=30, unique=True)
    voice_message_text = models.CharField(max_length=200)
    audio_file_name = models.CharField(max_length=30)
    image_file_name = models.CharField(max_length=30)

    def __str__(self):
        return self.voice_message_text


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    number = models.PositiveSmallIntegerField(unique=True)
    description = models.TextField(max_length=500)
    message = models.ForeignKey(to=Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class SCPoint(models.Model):
    lon = models.DecimalField(max_digits=11, decimal_places=8)  # longitude X
    lat = models.DecimalField(max_digits=11, decimal_places=8)  # latitude Y
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE)
    speed = models.PositiveSmallIntegerField(default=0)
    dirtype = models.PositiveSmallIntegerField(default=1)
    direction = models.SmallIntegerField  # Should it be Only Positive (0<)?
    add_date = models.DateTimeField('Date on which the SpeedCam was added')
    priority = models.PositiveSmallIntegerField(default=0)
    danger = models.BooleanField(default=False)
    method = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.type
