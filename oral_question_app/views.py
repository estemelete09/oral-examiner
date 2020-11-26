from django.shortcuts import render, reverse
import os
from django.http.response import StreamingHttpResponse
from .models import Voices, Avatars, Questions
from .camera import VideoCamera

#renders all the models or files uploaded in a form
def home(request):
	avatars= Avatars.objects.all()
	questions= Questions.objects.all()

	return render(request, 'home.html', 
		{'avatars': avatars ,
		'questions': questions
		})
#renders the submitted form from 'home'
def start(request):
	#pass the post data into a variable
	avatar = request.POST["avatar"]
	question = request.POST["question"]
	#look for the models with the same name and return as a file
	selected_avatar = Avatars.objects.get(avatarname=avatar)
	selected_question = Questions.objects.get(question=question)

	return render(request, 'start.html', 
		{'title': 'Start', 
		'selected_avatar': selected_avatar, 
		'selected_question': selected_question
		})

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')	 

def webcam_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
		content_type= 'multipart/x-mixed-replace; boundary=frame')	 