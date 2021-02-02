from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("start/", views.start, name="start"),
    path("webcam_feed", views.webcam_feed, name="webcam_feed"),
    path("start/speech_to_text/", views.speech_to_text, name="speech_to_text"),
    path("start/text_to_speech/", views.text_to_speech, name="text_to_speech"),
     path("start/check_answer/", views.check_answer, name="check_answer"),
] 

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)