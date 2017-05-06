from Person import Person

class SysAdmin(Person):
    __SAExp = 0
    
    def setSAExp(self, sx):
        self.__SAExp = sx
        
    def SAExp(self):
        return self.__SAExp
    
    def descriptionOfPerson(self):
        super().descriptionOfPerson()
        print("| Я системный администратор и мой опыт работы -", self.__SAExp, "лет!")