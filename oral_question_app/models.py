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

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        super(Voices, self).delete(*args, **kwargs)    

class Questions(models.Model):
    question = models.CharField(max_length=122)
    question_details = models.CharField(max_length=255)
    answer = models.CharField(max_length=122)
    # file = models.FileField(upload_to="questions/")

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question

    # def delete(self, *args, **kwargs):
    #         self.file.delete(save=False)
    #         super(Questions, self).delete(*args, **kwargs)        

class Avatars(models.Model):
    avatarname = models.CharField(max_length=122)
    file = models.FileField(upload_to="avatars/")

    class Meta:
        verbose_name_plural = 'Avatars'

    def __str__(self):
        return self.avatarname