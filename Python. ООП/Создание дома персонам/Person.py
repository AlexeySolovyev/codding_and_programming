class Person:
    
    __name = "n/a"
    __age = 0
    __address = "n/a"
    
    def __init__(self, n, a):
        self.__name = n
        self.__age = a
    
#     def setName(self, n):
#         self.__name = n
#         
#     def setAge(self, a):
#         self.__age = a
    
    def setAddress(self, adrs):
        self.__address = adrs
    
    def name(self):
        return self.__name
    
    def age(self):
        return self.__age
    
    def address(self):
        return self.__address
        
    def descriptionOfPerson(self):
        print(".................")
        print("| Привет! Меня зовут", self.__name + "!")
        print("| Мне", self.__age, "лет!")
        print('| Мой адрес "' + self.__address + '"!')
        
    
    @staticmethod
    def testStatic():
        print(__age)
        
    @classmethod
    def testClass(cls):
        print(cls.__age)