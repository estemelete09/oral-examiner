#speech to text function
def stt_process():
	import speech_recognition as sr
	# get audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		print("Test") #prints on terminal
	try:
		output = "" + r.recognize_google(audio)
	except sr.UnknownValueError:
		output = "Please Try again"
	except sr.RequestError as e:
		output = "Could not request results; {0}".format(e)

	audiodata =output
	print(audiodata) #prints on terminal
	return audiodata

#text to speech function
def tts_process(text):
	import pyttsx3
	engine = pyttsx3.init()

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)

	volume = engine.getProperty('volume')
	engine.setProperty('volume',1.0)

	rate = engine.getProperty('rate')   
	engine.setProperty('rate', 140)  

	print(text) #prints on terminal
	engine.say(text)
	engine.runAndWait()