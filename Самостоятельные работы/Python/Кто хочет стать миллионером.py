import random

won, won_now, user_answ, answer = 0, 0, "true", "false"

print('ПКШоу "Кто хочет стать миллионером?"')
print("Правила игры:")
print("Вашей задачей будет пройти 15 вопросов, состоящих из 4 ответов. Постепенно вы будете зарабатывать виртуальный приз.")
print("Также вы можете воспользоваться подзказками, вводя их в поле ответа: ")
print("Q - вы уходите из игры, сохраняя ваш приз; \n50:50 - подсказка 50:50 убирает два заведомо неверных ответа; \n2 - двойной ответ, дающий возможность ответить на вопрос дважды; \nСмена - смнеа текущего вопроса на другой, при этом вы не продвигаетесь дальше;")
print("Вы можете пользоваться всеми подсказками, но только один раз.")
input("Начнём?\n\n")


while quit != "Нет":
    hint50, hint2, hintChange = True, True, True
    hint50istrue, hint2istrue, incorrect_answer = False, False, False

    question_1 = ["Что растёт на огороде?", "Какое название телеканала верное?", "Сколько ног у паукообразных?"]
    question_2 = ['Назовите сокращённое название "маршрутного такси".', "Назовите популярного стихотворца.",
                  'Какого персонажа нет в известной считалке "На золотом крыльце сидели"?']
    question_3 = ['Назовите название популярной телепередачи на 1 канале. "Что? Где?..."',
                  "Какой телеканал существует на самом деле?",
                  "Где, если верить пословице, любопытной Варваре нос оторвали?"]
    question_4 = ["Какой отряд птиц не умеет летать?", "Какой предел медицинского градусника?",
                  "Сколько хромосом у среднестатистического человека?"]
    question_5 = ["Кто из 4-ёх мушкетёров был не назван? Атос, Д'Артаньян, Партос...", "Назовите формулу воды.",
                  "Какую обувь приобрёл к зиме Шарик из мультфильма про Простоквашино?"]
    question_6 = ["Назовите годы правления Михаила Фёдоровича Романова.",
                  "Когда произрошло Первое Московское ополчение?",
                  "Когда произшло крщение на Руси?"]
    question_7 = ["К какому семейству птиц относится снегирь?",
                  "Что испанцы съедают в новогоднюю полночь с каждым ударом часов?",
                  "В какую одежду принято плакать, чтобы вызвать сочувствие?"]
    question_8 = ["На практике при движении по кривой этот шарик делает 5000 оборотов в минуту, а при движении по прямой более 20000 оборотов в минуту. Где этот шарик находится?",
        		  'Как звали почтальона Печкина из мультфильма "Трое из Простоквашино"?',
        		  "Каким предметом китайцы стараются не пользоваться в преддверии Нового года, чтобы не разрушить счастья?"]
    question_9 = ["Из какого мяса традиционно готовится начинка для чебуреков?",
                  "Изучение соединений какого элемента является основой органической химии?",
                  "Разновидностью какого минерала является горный хрусталь?"]
    question_10 = ["В какое море впадает река Урал?", "Как называется шуточная поэма Пушкина?",
                   "С каким из этих государств не граничит Россия?"]
    question_11 = ["Как называется метеорный поток, наблюдаемый ежегодно в ноябре?",
                   "Как называется балет Дмитрия Шостоковича на производственную тематику?",
                   "Какого цвета были первые советские скафандры для космонавтов?"]
    question_12 = ["Чего боится охлофоб?",
                   "В кого богиня Афина превратила бросившую ей вызов ткачиху и вышивальщицу Арахну?",
                   "В каком море находятся Соловецкие острова?"]
    question_13 = ["Кто из наших соотечественников был первым удостоен звания Героя Советского Союза?",
                   "Каким русским императором многие считали загадочного старца Фёдора Кузьмича?",
                   "Какая планета Солнечной системы названа в честь деда древнеримского Юпитера и отца Сатурна?"]
    question_14 = ["Что в России 19 века делали в дортуаре?",
                   "Под каким флагом после успешных операций возвращаются в порт подводные лодки Великобритании?",
                   "Какой русский князь осадил столицу Византийской империи и наложил на империю контрибуцию?"]
    question_15 = ['Кто из этих философов в 1864 году написал музыку на стихи А. С. Пушкина "Заклинание" и "Зимний вечер"?',
        		   "Как назвали первую кимберлитовую трубку, открытую Ларисой Попугаевой 21 августа 1954 года?",
        		   "С какой буквы начинаются слова, опубликованные в 16 томе последнего издания Большой Советской Энциклопедии?"]

    random.shuffle(question_1)
    quest_1 = question_1[0]
    random.shuffle(question_2)
    quest_2 = question_2[0]
    random.shuffle(question_3)
    quest_3 = question_3[0]
    random.shuffle(question_4)
    quest_4 = question_4[0]
    random.shuffle(question_5)
    quest_5 = question_5[0]
    random.shuffle(question_6)
    quest_6 = question_6[0]
    random.shuffle(question_7)
    quest_7 = question_7[0]
    random.shuffle(question_8)
    quest_8 = question_8[0]
    random.shuffle(question_9)
    quest_9 = question_9[0]
    random.shuffle(question_10)
    quest_10 = question_10[0]
    random.shuffle(question_11)
    quest_11 = question_11[0]
    random.shuffle(question_12)
    quest_12 = question_12[0]
    random.shuffle(question_13)
    quest_13 = question_13[0]
    random.shuffle(question_14)
    quest_14 = question_14[0]
    random.shuffle(question_15)
    quest_15 = question_15[0]

    while True:

        # Вопрос №1
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №1. Стоимость: 500 рублей")

            if quest_1 == "Что растёт на огороде?":
                a = "Пистолет"
                b = "Лук"
                c = "Пулемёт"
                d = "Ракета СС-20"
                answer = ["B", "В"]
            elif quest_1 == "Какое название телеканала верное?":
                a = "СТС"
                b = "ТСТ"
                c = "CCT"
                d = "ЖЛОБ"
                answer = ["A", "А"]
            elif quest_1 == "Сколько ног у паукообразных?":
                a = "6"
                b = "8"
                c = "10"
                d = "12"
                answer = ["B", "В"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_1)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 500 руб.")
                won_now = 500
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 0 руб.")
                won_now = 0
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_1 = question_1[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 0
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №2
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №2. Стоимость: 1 000 рублей")

            if quest_2 == 'Назовите сокращённое название "маршрутного такси".':
                a = "Путёвка"
                b = "Курсовка"
                c = "Маршрутка"
                d = "Ватрушка"
                answer = ["C", "С"]
            elif quest_2 == "Назовите популярного стихотворца.":
                a = "Колотушкин"
                b = "Пушкин"
                c = "Васькин"
                d = "Петькин"
                answer = ["B", "В"]
            elif quest_2 == 'Какого персонажа нет в известной считалке "На золотом крыльце сидели"?':
                a = "Сапожник"
                b = "Король"
                c = "Портной"
                d = "Крестьянин"
                answer = ["D", "D"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_2)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 1 000 руб.")
                won_now = 1000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 500 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_2 = question_2[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 0
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №3
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №3. Стоимость: 2 000 рублей")

            if quest_3 == 'Назовите название популярной телепередачи на 1 канале. "Что? Где?..."':
                a = "Зачем?"
                b = "Как?"
                c = "Когда?"
                d = "Какой?"
                answer = ["С", "C"]
            elif quest_3 == "Какой телеканал существует на самом деле?":
                a = "Колесо обозрения"
                b = "Карусель"
                c = "Американские гонки"
                d = "Водное ралли"
                answer = ["B", "В"]
            elif quest_3 == "Где, если верить пословице, любопытной Варваре нос оторвали?":
                a = "В дверях"
                b = "На рынке"
                c = "На концерте"
                d = "На базаре"
                answer = ["D", "D"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_3)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 2 000 руб.")
                won_now = 2000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 1 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_3 = question_3[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 0
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №4
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №4. Стоимость: 3 000 рублей")

            if quest_4 == "Какой отряд птиц не умеет летать?":
                a = "Воробьинообразные"
                b = "Совы"
                c = "Страусы"
                d = "Журавлеобразные"
                answer = ["С", "C"]
            elif quest_4 == "Какой предел медицинского градусника?":
                a = "41"
                b = "42"
                c = "43"
                d = "44"
                answer = ["В", "B"]
            elif quest_4 == "Сколько хромосом у среднестатистического человека?":
                a = "44"
                b = "45"
                c = "46"
                d = "47"
                answer = ["С", "C"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_4)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 3 000 руб.")
                won_now = 3000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 2 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_4 = question_4[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 0
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №5
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №5. Стоимость: 5 000 рублей - несгораемая сумма.")

            if quest_5 == "Кто из 4-ёх мушкетёров был не назван? Атос, Д'Артаньян, Партос...":
                a = "Граф Де'ЛаФер"
                b = "Арамис"
                c = "Кардинал Ришелье"
                d = "Бекингем"
                answer = ["В", "B"]
            elif quest_5 == "Назовите формулу воды.":
                a = "H2O"
                b = "HO2"
                c = "O2H"
                d = "OH2"
                answer = ["A", "А"]
            elif quest_5 == "Какую обувь приобрёл к зиме Шарик из мультфильма про Простоквашино?":
                a = "Валенки"
                b = "Тапочки"
                c = "Кеды"
                d = "Ватники"
                answer = ["С", "C"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_5)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 5 000 руб. - ваша первая несгораемая сумма!")
                won_now = 5000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 3 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_5 = question_5[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 0
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №6
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №6. Стоимость: 10 000 рублей")

            if quest_6 == "Назовите годы правления Михаила Фёдоровича Романова.":
                a = "1613 - 1645 года"
                b = "1615 - 1643 года"
                c = "1645 - 1713 года"
                d = "1513 - 1545 года"
                answer = ["А", "A"]
            elif quest_6 == "Когда произрошло Первое Московское ополчение?":
                a = "1612 год"
                b = "1611 год"
                c = "1610 год"
                d = "1609 год"
                answer = ["В", "B"]
            elif quest_6 == "Когда произшло крщение на Руси?":
                a = "977 год"
                b = "988 год"
                c = "978 год"
                d = "987 год"
                answer = ["В", "B"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_6)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 10 000 руб.")
                won_now = 10000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 5 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_6 = question_6[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 5000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №7
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №7. Стоимость: 15 000 рублей")

            if quest_7 == "К какому семейству птиц относится снегирь?":
                a = "Вьюрковые"
                b = "Воробьиные"
                c = "Голубиные"
                d = "Жаворонковые"
                answer = ["A", "А"]
            elif quest_7 == "Что испанцы съедают в новогоднюю полночь с каждым ударом часов?":
                a = "Гуайяву"
                b = "Ежевику"
                c = "Виноградинку"
                d = "Гирры"
                answer = ["C", "С"]
            elif quest_7 == "В какую одежду принято плакать, чтобы вызвать сочувствие?":
                a = "В рукав"
                b = "В фартук"
                c = "В жилетку"
                d = "В рубашку"
                answer = ["C", "С"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_7)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 15 000 руб.")
                won_now = 15000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 10 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_7 = question_7[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 5000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №8
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №8. Стоимость: 25 000 рублей")

            if quest_8 == "На практике при движении по кривой этот шарик делает 5000 оборотов в минуту, а при движении по прямой более 20000 оборотов в минуту. Где этот шарик находится?":
                a = "Подшипник"
                b = "Шаровой сустав"
                c = "Шариковая ручка"
                d = "Шаровой двигатель"
                answer = ["С", "C"]
            elif quest_8 == 'Как звали почтальона Печкина из мультфильма "Трое из Простоквашино"?':
                a = "Фёдор Иванович"
                b = "Игорь Иванович"
                c = "Юрий Иванович"
                d = "Виктор Иванович"
                answer = ["B", "В"]
            elif quest_8 == "Каким предметом китайцы стараются не пользоваться в преддверии Нового года, чтобы не разрушить счастья?":
                a = "Мечом"
                b = "Вилкой"
                c = "Секирой"
                d = "Ножом"
                answer = ["D", "D"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_8)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 25 000 руб.")
                won_now = 25000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 15 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_8 = question_8[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 5000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №9
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №9. Стоимость: 50 000 рублей")

            if quest_9 == "Из какого мяса традиционно готовится начинка для чебуреков?":
                a = "Баранина"
                b = "Говядина"
                c = "Кура"
                d = "Свинина"
                answer = ["А", "A"]
            elif quest_9 == "Изучение соединений какого элемента является основой органической химии?":
                a = "Кислород"
                b = "Кремний"
                c = "Азот"
                d = "Углерод"
                answer = ["D", "D"]
            elif quest_9 == "Разновидностью какого минерала является горный хрусталь?":
                a = "Кварца"
                b = "Алмаза"
                c = "Кианита"
                d = "Лазурита"
                answer = ["А", "A"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_9)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 50 000 руб.")
                won_now = 50000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 25 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_9 = question_9[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 5000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №10
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №10. Стоимость: 100 000 рублей")

            if quest_10 == "В какое море впадает река Урал?":
                a = "Каспийское"
                b = "Чёрное"
                c = "Азовское"
                d = "Сердиземное"
                answer = ["А", "A"]
            elif quest_10 == "Как называется шуточная поэма Пушкина?":
                a = "Домик в Вероне"
                b = "Домик с колонной"
                c = "Домик в Коломне"
                d = "Домик на склоне"
                answer = ["С", "C"]
            elif quest_10 == "С каким из этих государств не граничит Россия?":
                a = "Грузия"
                b = "Узбекистан"
                c = "Казахстан"
                d = "Азербайджан"
                answer = ["В", "B"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_10)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 100 000 руб. - ваша вторая несгораемая сумма! До победы осталось 5 вопросов!")
                won_now = 100000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 50 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_10 = question_10[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 5000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №11
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №11. Стоимость: 200 000 рублей")

            if quest_11 == "Как называется метеорный поток, наблюдаемый ежегодно в ноябре?":
                a = "Максимы"
                b = "Леониды"
                c = "Гаврилы"
                d = "Иваны"
                answer = ["В", "B"]
            elif quest_11 == "Как называется балет Дмитрия Шостоковича на производственную тематику?":
                a = "Болт"
                b = "Винт"
                c = "Шайба"
                d = "Гайка"
                answer = ["A", "А"]
            elif quest_11 == "Какого цвета были первые советские скафандры для космонавтов?":
                a = "Жёлтого"
                b = "Голубого"
                c = "Белого"
                d = "Оранжевого"
                answer = ["D", "D"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_11)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 200 000 руб. До победы осталось 4 вопроса!")
                won_now = 200000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 100 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_11 = question_11[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 100000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №12
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №12. Стоимость: 400 000 рублей")

            if quest_12 == "Чего боится охлофоб?":
                a = "Змей"
                b = "Толпы"
                c = "Наказания"
                d = "Открытого пространства"
                answer = ["В", "B"]
            elif quest_12 == "В кого богиня Афина превратила бросившую ей вызов ткачиху и вышивальщицу Арахну?":
                a = "В жабу"
                b = "В рыбу"
                c = "В паука"
                d = "В змею"
                answer = ["С", "C"]
            elif quest_12 == "В каком море находятся Соловецкие острова?":
                a = "Балтийское"
                b = "Белое"
                c = "Карское"
                d = "Баренцево"
                answer = ["В", "B"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_12)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 400 000 руб. До победы осталось 3 вопроса!")
                won_now = 400000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 200 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_12 = question_12[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Вы были близки!")
                    print("Правильный ответ: " + answer[0])
                    won_now = 100000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №13
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №13. Стоимость: 800 000 рублей")

            if quest_13 == "Кто из наших соотечественников был первым удостоен звания Героя Советского Союза?":
                a = "Шмидт"
                b = "Ляпидевский"
                c = "Чкалов"
                d = "Водопьянов"
                answer = ["В", "B"]
            elif quest_13 == "Каким русским императором многие считали загадочного старца Фёдора Кузьмича?":
                a = "Александр I"
                b = "Павел I"
                c = "Николай I"
                d = "Александр II"
                answer = ["А", "A"]
            elif quest_13 == "Какая планета Солнечной системы названа в честь деда древнеримского Юпитера и отца Сатурна?":
                a = "Нептун"
                b = "Меркурий"
                c = "Марс"
                d = "Уран"
                answer = ["D", "D"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_13)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 800 000 руб. До победы осталось 2 вопроса!")
                won_now = 800000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 400 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_13 = question_13[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Вы были очень близки!")
                    print("Правильный ответ: " + answer[0])
                    won_now = 100000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №14
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №14. Стоимость: 1 500 000 рублей")

            if quest_14 == "Что в России 19 века делали в дортуаре?":
                a = "Спали"
                b = "Ели"
                c = "Купались"
                d = "Ездили верхом"
                answer = ["А", "A"]
            elif quest_14 == "Под каким флагом после успешных операций возвращаются в порт подводные лодки Великобритании?":
                a = "Флаг Вильгельма Завоевателя"
                b = "Флаг поверженного противника"
                c = "Белый флаг"
                d = 'Весёлый Роджер'
                answer = ["D", "D"]
            elif quest_14 == "Какой русский князь осадил столицу Византийской империи и наложил на империю контрибуцию?":
                a = "Олег Вещий"
                b = "Ярослав Мудрый"
                c = "Владимир Мономах"
                d = "Игорь"
                answer = ["C", "С"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_14)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПоздравляем! Ваш выигрыш: 1 500 000 руб. До победы остался 1 вопрос!")
                won_now = 1500000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 800 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_14 = question_14[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Очень жаль, ведь оставался один вопрос!")
                    print("Правильный ответ: " + answer[0])
                    won_now = 100000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

        # Вопрос №15
        while user_answ != answer[0] and user_answ != answer[1]:
            print("\nВопрос №15. Стоимость: 3 000 000 рублей")

            if quest_15 == 'Кто из этих философов в 1864 году написал музыку на стихи А. С. Пушкина "Заклинание" и "Зимний вечер"?':
                a = "Шопенгауэр"
                b = "Гегель"
                c = "Ницше"
                d = "Юнг"
                answer = ["C", "С"]
            elif quest_15 == "Как назвали первую кимберлитовую трубку, открытую Ларисой Попугаевой 21 августа 1954 года?":
                a = '"Удачная"'
                b = '"Зарница"'
                c = '"Мир"'
                d = '"Советская"'
                answer = ["B", "В"]
            elif quest_15 == "С какой буквы начинаются слова, опубликованные в 16 томе последнего издания Большой Советской Энциклопедии?":
                a = "Л"
                b = "М"
                c = "Н"
                d = "О"
                answer = ["B", "В"]

            if incorrect_answer:
                if user_answ == "A" or user_answ == "А":
                    a = ""
                elif user_answ == "B" or user_answ == "В":
                    b = ""
                elif user_answ == "C" or user_answ == "С":
                    c = ""
                elif user_answ == "D":
                    d = ""
                hint2istrue = False

            if hint50istrue:
                if answer[0] == "A":
                    c, d = "", ""
                elif answer[0] == "B":
                    a, d = "", ""
                elif answer[0] == "C":
                    a, b = "", ""
                elif answer[0] == "D":
                    a, c = "", ""

            print(quest_15)
            print("A - " + a)
            print("B - " + b)
            print("C - " + c)
            print("D - " + d)
            user_answ = input("\nВаш ответ: ")
            user_answ = user_answ.upper()
            if user_answ == answer[0] or user_answ == answer[1]:
                print("\nПриносим свои поздравления! Вы победитель нашей игры! Вы миллионер и ваш выигрыш составляет 3 000 000 рублей!")
                won_now = 3000000
                hint50istrue = False
                hint2istrue = False
                break
            elif user_answ == "Q":
                print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 1 500 000 руб.")
                break
            elif user_answ == "СМЕНА" and hintChange:
                print("Вопрос сменён!")
                quest_15 = question_15[1]
                hintChange = False
            elif user_answ == "СМЕНА" and not hintChange:
                print("К сожалению, подсказка Смена вопроса была уже использована!")
            elif user_answ == "50:50" and hint50:
                print("Два заведомо неверных ответа были убраны!")
                hint50istrue = True
                hint50 = False
            elif user_answ == "50:50" and not hint50:
                print("К сожалению, подсказка 50:50 была уже использована!")
            elif user_answ == "2" and hint2:
                print("Вам дано Право на ошибку!")
                hint2 = False
                hint2istrue = True
            elif user_answ == "2" and not hint2:
                print("К сожалению, вы уже использовали Право на ошибку!")
            else:
                if hint2istrue:
                    print("Это неверный ответ! Вам дан второй шанс!")
                    print("Если вы сейчас ответите неверно, то вы проиграете!")
                    incorrect_answer = True
                else:
                    print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Если бы вы ответили верно, то стали бы миллионером.")
                    print("Правильный ответ: " + answer[0])
                    won_now = 100000
                    break
        if user_answ != answer[0] and user_answ != answer[1]:
            break
        else:
            user_answ, answer = "true", "false"

    won += won_now
    print("Спасибо за игру! Вот сумма, которую вы выиграли за все игры: " + str(won) + " руб.")
    quit = input("Хотите сыграть ещё раз? (Да/Нет): ")
print("Удачи!")