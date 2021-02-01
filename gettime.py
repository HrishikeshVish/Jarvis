from datetime import datetime

def gettime():
	now = datetime.now()
	current_time = now.strftime("%H:%M")
	return current_time