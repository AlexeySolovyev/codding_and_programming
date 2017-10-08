class Person:
    
    __name = "n/a"
    __age = 0
    
    def setName(self, n):
        self.__name = n
        
    def setAge(self, a):
        self.__age = a
        
    def descriptionOfPerson(self):
        print("-----------------")
        print("| Hi! My name is", self.__name + "!")
        print("| I'm", self.__age, "years old!")