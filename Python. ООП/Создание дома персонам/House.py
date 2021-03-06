from Person import Person

class House:
    __address = "n/a"
    __listOfResidents = []
    
    def __init__(self, adrs):
        self.__address = adrs
    
#     def setAddress(self, adrs):
#         self.__address = adrs
        
    def address(self):
        return self.__address
    
    def settlePerson(self, p):
        if isinstance(p, Person):
            self.__listOfResidents.append(p)
            p.setAddress(self.__address)
    
    def evictPerson(self, p):
        self.__listOfResidents.remove(p)
        p._setAddress("n/a")
    
    def descriptionOfHouse(self):
        print(".................")
        print('| Адрес этого дома "' + self.__address + '".')
        print("| Здесь живут следующие жители: ")
        for i in self.__listOfResidents:
            print("|", i.name())