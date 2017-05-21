import vk
from VKBot import MyVKData
session = vk.Session()
vkapi = vk.API(session)

friends = vkapi.friends.get(user_id = MyVKData.userID, fields = "online")
print("Количество моих друзей: %d"%(len(friends)))
[print(i) for i in friends]
