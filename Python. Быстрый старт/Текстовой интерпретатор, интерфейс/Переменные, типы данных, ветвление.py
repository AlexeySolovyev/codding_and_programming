print("Переменные, типы данных, ветвления.")

#Переменные
name = input("Ваше имя:")
print("Привет, программист " + name + "!")
print("")
work = input("Давай поработаем? (Да/Нет/Не знаю)")

#Ветвление
if work == 'Да':
    print("Добро пожаловать в мир Python, " + name + "!")
    print(" ")
    work_user = input("Что хочешь сделать: (10 / 3, 10 % 3, 10 ** 3)")
    if work_user == '10 / 3':
        print(10 / 3)
        input()
    elif work_user == '10 % 3':
        print(10 % 3)
        input()
    elif work_user == '10 ** 3':
        print(10 ** 3)
        input()
elif work == 'Нет':
    print("До скорой встречи, " + name + "!")
    input()
elif work == 'Не знаю':
    print("Эх, " + name + "-" + name + ", лентяй ты!")
    input()
else:
    print("Неккоректный ввод!")
    input()

'''
Если необходимо оставить условие пустым, то мы пишем при определённом условии в действиях pass, что означает - "пропустить"
'''