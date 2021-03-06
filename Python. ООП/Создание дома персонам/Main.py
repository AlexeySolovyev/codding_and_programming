from Person import Person
from House import House
from Programmer import Programmer
from SystemAdmin import SysAdmin

print("Создаём мужчину и женщину...")
man = Person("Вася", 14)
woman = Person("Алиса", 15)

print("\nСоздаём программиста...")
programmer_man = Programmer("Костя", 27)
programmer_man.setProgExp(7)

print("\nСоздаём сисадмина...")
sysadmin_man = SysAdmin("Павел", 34)
sysadmin_man.setSAExp(12)


print("\nСоздаём дом...")
house = House("Москва, дом 2")



print("\nЗапрашиваем описание мужчины...")
man.descriptionOfPerson()
print("\nЗапрашиваем описание женщины...")
woman.descriptionOfPerson()
print("\nЗапрашиваем описание программиста...")
programmer_man.descriptionOfPerson()
print("\nЗапрашиваем описание сисадмина...")
sysadmin_man.descriptionOfPerson()
# print("\nЗапрашиваем описание дома...")
# house.descriptionOfHouse()



# print("\nЗадаём дому адрес...")
# house.setAddress("Москва, дом 2")

# print("\nЗапрашиваем описание дома...")
# house.descriptionOfHouse()




# print("\nЗадаём мужчине имя, возраст и дом...")
# man.setName("Вася")
# man.setAge("14")
house.settlePerson(man)


# print("\nИ запрашиваем его описание...")
# man.descriptionOfPerson()


# print("\nЗадаём женщине имя, возраст и дом...")
# woman.setName("Алиса")
# woman.setAge("15")
house.settlePerson(woman)

# print("\nИ запрашиваем её описание...")
# woman.descriptionOfPerson()


print("\nИ, наконец, запрашиваем описание дома...")
house.descriptionOfHouse()