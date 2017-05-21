logANDpass = open("C:/logANDpass.txt", "r").read()

class MyVkData:
	userID = "165504240"
	DurovUserID = "1"
	apiUrl = "https://api.vk.com/method/"
	appID = 6033657
	login = logANDpass[0:12]
	password = logANDpass[12:31]