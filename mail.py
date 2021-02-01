import smtplib
import knowledge_base
  

def mail(name, message):
	id = knowledge_base.getMailId(name)
	if id:
		# creates SMTP session 
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		  
		# start TLS for security 
		s.starttls() 
		  
		# Authentication 
		s.login("msavinash1139@gmail.com", "aavviinnaasshh123") 
		  
		# message to be sent 
		# message = "Hello. This is JARVIS."
		  
		# sending the mail 
		print("SEE ME:", message)
		s.sendmail("msavinash1139@gmail.com", id, message) 
		  
		# terminating the session 
		s.quit()
		return "done" 
	else:
		return ""