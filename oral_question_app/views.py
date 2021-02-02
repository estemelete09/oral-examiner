from django.shortcuts import render, reverse
import os
from django.http.response import StreamingHttpResponse
from .models import Voices, Avatars, Questions
from .camera import VideoCamera
from .functions import stt_process,tts_process
from django.http import HttpResponse
import json
from django.http import JsonResponse

#renders all the models or files uploaded in a form
def home(request):
    avatars= Avatars.objects.all()
    # questions= Questions.objects.all()

    return render(request, 'home.html', {
        'avatars': avatars ,
        # 'questions': questions
        })
#renders the submitted form from 'home'
def start(request):
    answer=""
    if request.method == "POST":
        #pass the post data into a variable
        avatar = request.POST["avatar"]
        #select the chosen avatar
        selected_avatar = Avatars.objects.get(avatarname=avatar)
        #select all questions saved on the database and pass on a variable
        questions= Questions.objects.all()
        
    return render(request, 'start.html', {
        'title': 'Start',
        'selected_avatar': selected_avatar, 
        'questions': questions
        })

#Speech To Text Function runs on clicking "answerbutton" button. Record the user's answer
def speech_to_text(request):
    audiodata= stt_process()    #function from functions.py
    return JsonResponse({
    'audiodata': audiodata,
    })

#Text to Speech Function runs on clicking "playquestion" button. Plays the question as audio
def text_to_speech(request):
    question_field = request.GET.get('getdata')
    questionfield = Questions.objects.get(question=question_field)
    question_details= questionfield.question_details
    tts_process(question_details)   #function from functions.py
    return JsonResponse(request.GET)

#runs on clicking "checkbutton" button. Compares the user's answer to the answer in database
def check_answer(request):
    question_field = request.GET.get('questiondata')
    answer_input = request.GET.get('answerdata')
    questionfield = Questions.objects.get(question=question_field)
    answer= questionfield.answer
    findtext= answer_input.find(answer)
    result_text= ''
    #audio plays whether the answer submitted is empty, correct or wrong
    if answer_input== '':
        result_text= "{}: Please record an answer!".format(questionfield)
        tts_process("So you don't have any idea? Try guessing.")
    elif findtext >= 0:
        result_text= "{}: Your Answer is Correct!".format(questionfield) 
        tts_process("You are correct! The answer is {}".format(answer)) 
    else:
        result_text= "{}: Wrong Answer!".format(questionfield)
        tts_process("Wrong answer, do you have another idea?")  

    return JsonResponse({
        'result_text' : result_text
        })

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')  
             
#webcam display
def webcam_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
        content_type= 'multipart/x-mixed-replace; boundary=frame')   
  
