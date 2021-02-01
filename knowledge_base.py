# from pymongo import MongoClient
# from pprint import pprint

# # Choose the appropriate client
# client = MongoClient()

# # Connect to the test db 
# db=client.test

# # Use the employee collection
# employee = db.employee
# employee_details = {
#     'Name': 'Raj Kumar',
#     'Address': 'Sears Streer, NZ',
#     'Age': '42'
# }

# # Use the insert method
# result = employee.insert_one(employee_details)

# # Query for the inserted document.
# Queryresult = employee.find_one({'Age': '42'})
# pprint(Queryresult)




from tinydb import TinyDB, Query
db = TinyDB('db.json')

personel = db.table("Personel")
projects = db.table("Projects")
personel.insert({"name":"jack", "mailId":"manojpissay@gmail.com"})
projects.insert({"url":"https://github.com/Sachetan-Sabhahit/", "reponame":"hello-world"})
def getMailId(name):
	# res = personel.search(name=name)
	# print(res)
	User = Query()
	# Search for a field value
	res = personel.search(User.name == name)
	try:
		return res[0]["mailId"]
	except IndexError:
		return

def getGitUrl(repo):
	Repo = Query()
	res = projects.search(Repo.reponame == repo)
	try:
		return res[0]["url"]
	except IndexError:
		return

# print(getMailId("asa"))