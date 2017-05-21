import vk
from VKBot import MyVKData
session = vk.AuthSession(app_id = MyVKData.appID, user_login = MyVKData.login, user_password = MyVKData.password)
vkapi = vk.API(session)

groups = vkapi.groups.get(user_id = MyVKData.userID, extended = 1)
[print(i) for i in groups]