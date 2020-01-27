from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from languages_plus.models import Language
# Create your models here.

'''
class MyLanguage(models.Model):
    alpha_3 = models.CharField(verbose_name='Short language name', max_length=3, unique=True, null=True)
    name = models.CharField(verbose_name='Language name', max_length=30, blank=True)  # , default='English'
    country = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.alpha_3} ({self.name})'
'''


class MyUser(models.Model):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # first_name = models.CharField(max_length=100, blank=True)
    # last_name = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}, {self.company}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class SCType(models.Model):
    name = models.CharField(verbose_name='SpeedCam code name', max_length=100, unique=True)
    number = models.PositiveSmallIntegerField(verbose_name='SpeedCam type number', unique=True)
    description = models.TextField(verbose_name='SpeedCam description', max_length=200, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    # message = models.ForeignKey(to=Message, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Type: {str(self.number)}; {self.description}'


class Message(models.Model):
    sc_type = models.ForeignKey(to=SCType, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE, null=True)
    message = models.CharField(verbose_name='Voice message text', max_length=200, blank=True)
    audio_file_name = models.CharField(max_length=30, blank=True)
    image_file_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.message


class Method(models.Model):
    name = models.CharField(verbose_name='Method name', max_length=30, unique=True, default=False)

    def __str__(self):
        return self.name


class SCPoint(models.Model):
    lon = models.DecimalField(verbose_name='Longitude (X)', max_digits=11, decimal_places=8)  # , default=0
    lat = models.DecimalField(verbose_name='Latitude (Y)', max_digits=11, decimal_places=8)
    type = models.ForeignKey(verbose_name='SpeedCam Type', to=SCType, on_delete=models.CASCADE)
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
        return f'ID: {str(self.id)}; Type: {str(self.type.number)}; self.type.description'
