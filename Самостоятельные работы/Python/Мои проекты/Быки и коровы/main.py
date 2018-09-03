import random

want_quit = ''

print('Игра "Быки и коровы"')
print("Правила игры: "
      "\nКомпьютер загадывает 4-значное число с неповторяющимися цифрами, а ваша задача его угадать. "
      "\nВам будут предложены подсказки: быки и коровы. "
      "\nКак только вы введёте ответ, вам покажут кол-во быков и коров. "
      "\nБыки - цифры, которые содержутся в загаднном числе и стоят на своих позициях. "
      "\nКоровы - цифры, которые содержутся в загаданном числе, но стоят не на своих местах. "
      "\nВам даны 10 попыток. Вперёд!")

while want_quit != "Y":

    nums = range(10)
    random.shuffle(nums)
    answer = str(nums[0] + nums[1] + nums[2] + nums[3])

    # print(answer) В качестве подсказки

    try_count = 10
    bulls, cows, number = 0, 0, 0

    while try_count != 0 and number != "q" and bulls != 4:

        number = input("Ваш ответ (для выхода - q): ")
        if number == "q": break

        bulls, cows = 0, 0

        if number[0] == answer[0]: bulls += 1
        if number[1] == answer[1]: bulls += 1
        if number[2] == answer[2]: bulls += 1
        if number[3] == answer[3]: bulls += 1

        if number[0] == answer[1] or number[0] == answer[2] or number[0] == answer[3]: cows += 1
        if number[1] == answer[2] or number[1] == answer[3] or number[1] == answer[0]: cows += 1
        if number[2] == answer[3] or number[2] == answer[0] or number[2] == answer[1]: cows += 1
        if number[3] == answer[0] or number[3] == answer[1] or number[3] == answer[2]: cows += 1

        try_count -= 1

        print('Быков: ' + str(bulls))
        print('Коров: ' + str(cows))

    if number == "q":
        break

    if try_count == 0:
        print("Попытки закончились! Вы проиграли!")
        lose += 1
    else:
        print("Поздравляем! Вы выиграли!")
        print("Потрачено: " + str(was_try) + " попыток!")

    want_quit = input("Хотите выйти? (Y/N): ").upper()
print("Спасибо за игру!")
input()
