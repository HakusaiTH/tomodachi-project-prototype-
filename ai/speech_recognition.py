import speech_recognition as sr
from gtts import gTTS 
from playsound import playsound 
from datetime import datetime 


r = sr.Recognizer()

with sr.Microphone() as source: 
	while(True) :
		audio = r.record(source, duration=5)


		try:
			text = r.recognize_google(audio, language="th") 

		except:
			text = "ขอโทษค่ะ"
		tts = gTTS(text, lang="th")