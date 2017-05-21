import vk
from VKBot import MyVKData
textMessage = open("textMessage.txt", "r")

session = vk.AuthSession(app_id = MyVKData.appID, user_login = MyVKData.login, user_password = MyVKData.password, scope = "wall")
vkapi = vk.API(session)

vkapi.wall.post(message = textMessage.read())