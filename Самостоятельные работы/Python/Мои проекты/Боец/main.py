from random import *
from time import *

name1, name2, difficult = "", "", ""
while name1 == "":
    name1 = input("Введите имя игрока №1: ")
while name2 == "":
    name2 = input("Введите имя игрока №2: ")

while difficult == "":
    difficult = input("\nСложности: \n"
                      "1. Лёгкий - у обоих по 15 жизней. \n"
                      "2. Средний - у обоих по 20 жизней. \n"
                      "3. Сложный - у обоих по 30 жизней. \n"
                      "Выберите сложность: ")
    if difficult == "1":
        player1, player2 = 15, 15
    elif difficult == "2":
        player1, player2 = 20, 20
    elif difficult == "3":
        player1, player2 = 30, 30

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("--------------------------------------------------------------------------------")
print('                                  ИГРА "БОЕЦ"                                   ')
print("--------------------------------------------------------------------------------")
print("                                  ПРАВИЛА ИГРЫ                                  ")
print("Вы - боец, вышедший на ринг. Ваша задача победить противника. У обоих " + str(player1) + " жизней."
      "Один раунд - это один ваш ход и один ход противника. \n"
      "За один ход вы можете совершить одно действие: \n"
      "1. Удар рукой - оценивается в 1 балл. \n"
      "2. Удар ногой - оценивается в 2 балла. \n"
      "3. Поставить блок - защищает вас от удара (крит. - кол-во баллов делится на 2). "
      "Номер действия соответствует порядковому номеру выше. \n"
      "После вашего хода ход переходит проитвнику. \n\n"
      "Далее определяется, какими получились ваш удар и удар противника. Может быть: \n"
      "1. Промах (20%). \n"
      "2. Засчитывается только удар рукой, промах ногой (40%). \n"
      "3. Засчитывается любой удар, будь то ногой или рукой (30%). \n"
      "4. Критический удар - удваивает силу удара (10%).")
print("--------------------------------------------------------------------------------")
input("Нажмите Enter для продолжения...")

battle, numKick1, numKick2 = 1, 0, 0

while (player1 > 0) and (player2 > 0):
    print("РАУНД " + str(battle))
    print(str(player1) + "   " + str(player2))
    print("\nНАЧАЛО УДАРОВ!")
    while (numKick1 != "1") and (numKick1 != "2") and (numKick1 != "3"):
        numKick1 = input(name1 + " - ваш удар: ")
    while (numKick2 != "1") and (numKick2 != "2") and (numKick2 != "3"):
        numKick2 = input(name2 + " - ваш удар: ")
    print("\nОЦЕНКА ПОПАДАНИй!")
    rand1 = randint(0, 10)
    rand2 = randint(0, 10)

    #                                                         ДЛЯ ИГРОКА №1
    if numKick1 == "1":
        if 3 <= rand1 <= 9:
            res1 = "Успешный удар рукой!"
            kick1 = 1
            if 15 > battle >= 10:
                kick1 += 1
            elif 20 > battle >= 15:
                kick1 += 2
            elif 25 > battle >= 20:
                kick1 += 3
            elif battle >= 25:
                kick1 += 4
        elif rand1 == 10:
            kick1 = 2
            res1 = "КРИТИЧЕСКИЙ удар рукой!"
            if 15 > battle >= 10:
                kick1 += 1
            elif 20 > battle >= 15:
                kick1 += 2
            elif 25 > battle >= 20:
                kick1 += 3
            elif battle >= 25:
                kick1 += 4
        else:
            kick1 = 0
            res1 = "Промах рукой!"
    elif numKick1 == "2":
        if 7 <= rand1 <= 9:
            kick1 = 2
            res1 = "Успешный удар ногой!"
            if 15 > battle >= 10:
                kick1 += 1
            elif 20 > battle >= 15:
                kick1 += 2
            elif 25 > battle >= 20:
                kick1 += 3
            elif battle >= 25:
                kick1 += 4
        elif rand1 == 10:
            kick1 = 4
            res1 = "КРИТИЧЕСКИЙ удар ногой!"
            if 15 > battle >= 10:
                kick1 += 1
            elif 20 > battle >= 15:
                kick1 += 2
            elif 25 > battle >= 20:
                kick1 += 3
            elif battle >= 25:
                kick1 += 4
        else:
            kick1 = 0
            res1 = "Промах ногой!"

        #                                                         ДЛЯ ИГРОКА №2
    if numKick2 == "1":
        if 3 <= rand2 <= 9:
            kick2 = 1
            res2 = "Успешный удар рукой!"
            if 15 > battle >= 10:
                kick2 += 1
            elif 20 > battle >= 15:
                kick2 += 2
            elif 25 > battle >= 20:
                kick2 += 3
            elif battle >= 25:
                kick2 += 4
        elif rand2 == 10:
            kick2 = 2
            res2 = "КРИТИЧЕСКИЙ удар рукой!"
            if 15 > battle >= 10:
                kick2 += 1
            elif 20 > battle >= 15:
                kick2 += 2
            elif 25 > battle >= 20:
                kick2 += 3
            elif battle >= 25:
                kick2 += 4
        else:
            kick2 = 0
            res2 = "Промах рукой!"
    elif numKick2 == "2":
        if 7 <= rand2 <= 9:
            kick2 = 2
            res2 = "Успешный удар ногой!"
            if 15 > battle >= 10:
                kick2 += 1
            elif 20 > battle >= 15:
                kick2 += 2
            elif 25 > battle >= 20:
                kick2 += 3
            elif battle >= 25:
                kick2 += 4
        elif rand2 == 10:
            kick2 = 4
            res2 = "КРИТИЧЕСКИЙ удар ногой!"
            if 15 > battle >= 10:
                kick2 += 1
            elif 20 > battle >= 15:
                kick2 += 2
            elif 25 > battle >= 20:
                kick2 += 3
            elif battle >= 25:
                kick2 += 4
        else:
            kick2 = 0
            res2 = "Промах ногой!"

    if numKick1 == "3":
        if rand2 != 10:
            kick2 = 0
            res1 = "Успешная защита!"
        else:
            kick2 /= 2
            if 15 > battle >= 10:
                kick2 += 1
            elif 20 > battle >= 15:
                kick2 += 2
            elif 25 > battle >= 20:
                kick2 += 3
            elif battle >= 25:
                kick2 += 4
            res1 = "Защита была сломлена!"

    if numKick2 == "3":
        if rand1 != 10:
            kick1 = 0
            res2 = "Успешная защита!"
        else:
            kick1 /= 2
            if 15 > battle >= 10:
                kick2 += 1
            elif 20 > battle >= 15:
                kick2 += 2
            elif 25 > battle >= 20:
                kick2 += 3
            elif battle >= 25:
                kick2 += 4
            res2 = "Защита была сломлена!"

    print(name1 + " ...")
    sleep(3)
    print(res1)

    print(name2 + " ...")
    sleep(3)
    print(res2)

    if 15 >battle >= 10:
        print("\nВ игре больше 10 раундов!")
        print("Урон увеличен на 1 балл!\n")
    elif 20 > battle >= 15:
        print("\nВ игре больше 15 раундов!")
        print("Урон увеличен на 2 балл!\n")
    elif 25 > battle >= 20:
        print("\nВ игре больше 20 раундов!")
        print("Урон увеличен на 3 балл!\n")
    elif battle >= 25:
        print("\nВ игре больше 25 раундов!")
        print("Урон увеличен на 4 балл!\n")

    player1 -= kick2
    player2 -= kick1

    print("\nРАУНД " + str(battle) + " ЗАВЕРШЁН!")
    battle += 1
    kick1, numKick1, kick2, numKick2 = 0, 0, 0, 0
    input("Нажмите Enter для прододжения...\n\n")

print("--------------------------------------------------------------------------------")
if (player1 <= 0) and (player2 > 0):
    print("                        ПОЗДРАВЛЯЕМ ИГРОКА {} С ПОБЕДОЙ!".format(name2.upper()))
elif (player2 <= 0) and (player1 > 0):
    print("                        ПОЗДРАВЛЯЕМ ИГРОКА {} С ПОБЕДОЙ!".format(name1.upper()))
else:
    print("                        ПОЗДРАВЛЯЕМ ИГРОКОВ! У ВАС НИЧЬЯ!")

input()
