from django.db import models
from django.conf import settings
import os.path

# Create your models here.
class Voices(models.Model):
    voicename = models.CharField(max_length=122)
    file = models.FileField(upload_to="voices/")

    class Meta:
        verbose_name_plural = 'Voices'

    def __str__(self):
        return self.voicename

class Questions(models.Model):
    question = models.CharField(max_length=122)
    file = models.FileField(upload_to="questions/")

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question

class Avatars(models.Model):
    avatarname = models.CharField(max_length=122)
    file = models.FileField(upload_to="avatars/")

    class Meta:
        verbose_name_plural = 'Avatars'

    def __str__(self):
        return self.avatarname