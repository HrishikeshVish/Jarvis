import wit
import translator
import gettime
import text_to_speech
import mail
from random import choice
import folderlist
import gitread
import debugger
import gitread

didnt_understand = ["Can you repeat that?", "Come again", "I did not seem to understand that"]



while 1:
	text = wit.getdata()
	print(text)
	comm = translator.translate(text["_text"])
	print(comm)

	if comm["command"] == "passive":
		pass

	elif comm["command"] == "time":
		t = gettime.gettime()
		text_to_speech.speak(t)

	elif comm["command"] == "mail":
		name = comm["reciepient"]
		text_to_speech.speak("Please provide a message")
		message = wit.getdata()["_text"]
		print("IN HUB:", message)
		res = mail.mail(name, message)
		print("FROM MAIL:", res)
		if res:
			print("SENT")
			# text_to_speech.speak("Message sent")
		else:
			text_to_speech.speak("Seems that " + name + "doesn't exist")


	elif comm["command"] == "debug":
		# text = wit.getdata()
		# error = translator.translate(text["_text"])
		error = comm["command"]
		resp = debugger.debug(error)
		print(resp)

	elif comm["command"] == "git":
		res = gitread.git(comm["reponame"])


	elif comm["command"] == "open":
		fname = comm["filename"]
		folderlist.ls(fname)


	elif comm["command"] == "shutdown":
		text_to_speech.speak("Until next time!")
		exit(0)

	else:
		s = choice(didnt_understand)
		text_to_speech.speak(s)