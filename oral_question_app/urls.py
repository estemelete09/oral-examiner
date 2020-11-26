from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/start/", views.start, name="start"),
    path("webcam_feed", views.webcam_feed, name="webcam_feed"),
] 

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)