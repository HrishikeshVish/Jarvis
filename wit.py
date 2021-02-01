import speech
import recognize

def getdata():
	text = speech.RecognizeSpeech("myspeech.wav", 4)
	text = recognize.recognize()
	return text