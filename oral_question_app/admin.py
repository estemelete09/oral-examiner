from django.contrib import admin
from .models import Voices, Avatars, Questions

# Register your models here.   
admin.site.register(Voices)
admin.site.register(Avatars)
admin.site.register(Questions)