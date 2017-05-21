import vk
from VKBot import MyVKData
import time

def sendUser(ms):
	vkapi.messages.send(user_id = messages[n]["uid"], message = ms)
def sendChat(idchat, ms):
	vkapi.messages.send(chat_id = idchat, message = ms)

session = vk.AuthSession(app_id = MyVKData.appID, user_login = MyVKData.login, user_password = MyVKData.password, scope = "messages")
vkapi = vk.API(session)

while True:
	time.sleep(2)
	messages = vkapi.messages.get(time_offset = 1)
	for n in range(1, len(messages)):
		textMessage = messages[n]["body"].lower()
		print(messages[n])
		if messages[n]["title"] == " ... ":
			if textMessage.find("привет") != -1:
				sendUser("Привет!")
			if textMessage.find("как дела") != -1:
				sendUser("Всё норм. А у тебя?")
		elif messages[n]["title"] == "7Б v2.0":
			if textMessage.find("какое") != -1 or textMessage.find("дз") != -1:
				sendChat(53, "Всё ДЗ здесь: https://trello.com/b/qFmlrUaW")