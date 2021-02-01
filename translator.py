def translate(text):
	print("HERE:", text)
	print("goodbye" in text)
	input_text = text.lower()
	tokens = input_text.split(" ")
	query = {'command':0}
	trig_start = "jarvis"
	if trig_start not in text:
		query["command"] = "passive"


	elif "goodbye" in text:
		query["command"] = "shutdown"
		print(query)


	elif(len(tokens)<=8 and ('what' in tokens or 'tell' in tokens) and 'time' in input_text):
		query['command'] = 'time'
		print(query)
	    
	    
	elif('wrong' in tokens or 'error' in tokens):
		query['command'] = 'debug'
		query['error'] = " ".join(tokens[tokens.index("error")+2:])
		print(query)


	elif('email' in tokens or 'mail' in tokens or ('write' in tokens and 'mail' in tokens)):
		query['command'] = 'mail'
		if('email' in tokens):
			query['reciepient'] = tokens[tokens.index('email')+2]
			print(query)
		else:
			query['reciepient'] = tokens[tokens.index('mail')+2]
			print(query)


	elif('open' in tokens):
		query['command'] = 'open'
		query['filename'] = tokens[tokens.index('open')+1]


	elif "clone" in tokens:
		query["command"] = "git"
		query['reponame'] = "-".join(tokens[len(tokens)+2:])

	return query

    
    
