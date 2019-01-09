from random import *
from textwork import *

def fighter(health1, health2):
    player1, player2 = health1, health2
    numKick1, numKick2 = 0, 0

    while (player1 > 0) and (player2 > 0):
        cnt('Здоровье соперников', 'center')
        cnt(str(player1) + "    " + str(player2), 'center')
        cnt("НАЧАЛО УДАРОВ!", 'center')
        numKick1 = quest('\nУдар Майкла: ', 'Удар рукой', 'Удар ногой', 'Защититься')
        numKick2 = randint(1, 3)
        if player2 <= 5: numKick2 = 3
        print('Удар Йохана: \n[1] - Удар рукой\n[2] - Удар ногой\n[3] - Защититься\nВаш ответ: ', end='')
        time.sleep(1.5)
        print(numKick2)
        rand1 = randint(0, 10)
        rand2 = randint(0, 10)

        #                                                         ДЛЯ ИГРОКА №1
        if numKick1 == 1:
            if 3 <= rand1 <= 9:
                res1 = "Успешный удар рукой!"
                kick1 = 2
            elif rand1 == 10:
                kick1 = 4
                res1 = "КРИТИЧЕСКИЙ удар рукой!"
            else:
                kick1 = 0
                res1 = "Промах рукой!"
        elif numKick1 == 2:
            if 7 <= rand1 <= 9:
                kick1 = 3
                res1 = "Успешный удар ногой!"
            elif rand1 == 10:
                kick1 = 6
                res1 = "КРИТИЧЕСКИЙ удар ногой!"
            else:
                kick1 = 0
                res1 = "Промах ногой!"

        #                                                         ДЛЯ ИГРОКА №2
        if numKick2 == 1:
            if 3 <= rand2 <= 9:
                kick2 = 2
                res2 = "Успешный удар рукой!"
            elif rand2 == 10:
                kick2 = 4
                res2 = "КРИТИЧЕСКИЙ удар рукой!"
            else:
                kick2 = 0
                res2 = "Промах рукой!"
        elif numKick2 == 2:
            if 7 <= rand2 <= 9:
                kick2 = 3
                res2 = "Успешный удар ногой!"
            elif rand2 == 10:
                kick2 = 6
                res2 = "КРИТИЧЕСКИЙ удар ногой!"
            else:
                kick2 = 0
                res2 = "Промах ногой!"

        if numKick1 == 3:
            if rand2 != 10:
                kick2 = 0
                res1 = "Успешная защита!"
            else:
                kick2 //= 2
                res1 = "Защита была сломлена!"

        if numKick2 == 3:
            if rand1 != 10:
                kick1 = 0
                res2 = "Успешная защита!"
            else:
                kick1 //= 2
                res2 = "Защита была сломлена!"

        time.sleep(1.5)
        print('Майкл:', res1)
        print('Йохан:', res2)

        player1 -= kick2
        player2 -= kick1

        kick1, numKick1, kick2, numKick2 = 0, 0, 0, 0
        if player1 > 0 and player2 > 0:
            wait('Нажмите для начала следующей атаки...')
        else:
            if player1 < 0:
                player1 = 0
            if player2 < 0:
                player2 = 0
            cnt('Здоровье соперников', 'center')
            cnt(str(player1) + "    " + str(player2), 'center')

    if player2 <=0:
        return True
    else:
        return False