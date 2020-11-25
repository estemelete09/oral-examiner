from django.shortcuts import render, reverse
import os
from django.http import HttpResponse
from .models import Voices, Avatars, Questions
from django import forms

def home(request):
	avatars= Avatars.objects.all()
	questions= Questions.objects.all()

	return render(request, 'home.html', 
		{'avatars': avatars, 
		'questions': questions
		})

def start(request):
	avatar = request.POST["avatar"]
	question = request.POST["question"]

	selected_avatar = Avatars.objects.get(avatarname=avatar)
	selected_question = Questions.objects.get(question=question)

	return render(request, 'start.html', 
		{'title': 'Start', 
		'selected_avatar': selected_avatar, 
		'selected_question': selected_question
		})
	# return HttpResponse('start')
	 # return HttpResponseRedirect(reverse("start"))