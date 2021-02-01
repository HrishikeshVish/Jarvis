import os



def ls(name):
	path = "D:/"
	flag = 0
	for root, dirs, files in os.walk(path):
		# dirs = [i.lower() for i in dirs]
		#print(dirs, name)
		path2 = ""
		if name in dirs:
			flag = 1
			path2 = os.path.join(root, name)
			break
	if flag:
		print(os.listdir(path2))
	

		#if name in dirs:

		#	print("HELLO YALL!")
		#	for root2, dirs2, files2 in os.walk(name):
		#		print(dirs2)
		#		print(files2)
