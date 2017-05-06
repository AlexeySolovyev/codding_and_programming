from Person import Person

class Programmer(Person):
    __progExp = 0
    
    def setProgExp(self, px):
        self.__progExp = px
        
    def ProgExp(self):
        return self.__progExp
    
    def descriptionOfPerson(self):
        super().descriptionOfPerson()
        print("| Я программист и мой опыт работы -", self.__progExp, "лет!")