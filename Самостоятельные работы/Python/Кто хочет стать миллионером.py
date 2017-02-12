import random

won = 0

print('ПКШоу "Кто хочет стать миллионером?"')
print("Правила игры:")
print("Вашей задачей будет пройти 15 вопросов, состоящих из 4 ответов. Постепенно вы будете зарабатывать виртуальный приз.")
print("Также вы можете воспользоваться подзказками, вводя их в поле ответа: ")
print("Q - вы уходите из игры, сохраняя ваш приз; \n50 - подсказка 50:50 убирает два заведомо неверных ответа; \n2 - двойной ответ, дающий возможность ответить на вопрос дважды; \nСмена - меняет текущий вопрос на другой;")
print("Вы можете пользоваться всеми подсказками, но только один раз.")
input("Начнём?")


while quit != "Нет":

    question_1 = ["Что растёт на огороде?", "Какое название телеканала верное?", "Сколько ног у паукообразных?"]
    question_2 = ['Назовите сокращённое название "маршрутного такси".', "Назовите популярного стихотворца.",
                  'Какого персонажа нет в известной считалке "На золотом крыльце сидели"? ']
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

    quest_1 = random.choice(question_1)
    quest_2 = random.choice(question_2)
    quest_3 = random.choice(question_3)
    quest_4 = random.choice(question_4)
    quest_5 = random.choice(question_5)
    quest_6 = random.choice(question_6)
    quest_7 = random.choice(question_7)
    quest_8 = random.choice(question_8)
    quest_9 = random.choice(question_9)
    quest_10 = random.choice(question_10)
    quest_11 = random.choice(question_11)
    quest_12 = random.choice(question_12)
    quest_13 = random.choice(question_13)
    quest_14 = random.choice(question_14)
    quest_15 = random.choice(question_15)

    while True:

        # Вопрос №1
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 500 руб.")
            won_now = 500
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
            break

        # Вопрос №2
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
        elif quest_2 == 'Какого персонажа нет в известной считалке "На золотом крыльце сидели"? ':
            a = "Сапожник"
            b = "Король"
            c = "Портной"
            d = "Крестьянин"
            answer = ["D", "D"]

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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 1000 руб.")
            won_now = 1000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
            break

        # Вопрос №3
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 2000 руб.")
            won_now = 2000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
            break

        # Вопрос №4
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 3000 руб.")
            won_now = 3000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
            break

        # Вопрос №5
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 5000 руб.")
            won_now = 5000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 0 руб.")
            break

        # Вопрос №6
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 10000 руб.")
            won_now = 10000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
            won_now = 5000
            break

        # Вопрос №7
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 15000 руб.")
            won_now = 15000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
            won_now = 5000
            break

        # Вопрос №8
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 25000 руб.")
            won_now = 25000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
            won_now = 5000
            break

        # Вопрос №9
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 50000 руб.")
            won_now = 50000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
            won_now = 5000
            break

        # Вопрос №10
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
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 100000 руб.")
            won_now = 100000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 5 000 руб.")
            won_now = 5000
            break

        # Вопрос №11
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

        print("\n" + quest_11)
        print("A - " + a)
        print("B - " + b)
        print("C - " + c)
        print("D - " + d)
        user_answ = input("\nВаш ответ: ")
        user_answ = user_answ.upper()
        if user_answ == answer[0] or user_answ == answer[1]:
            print("\nПоздравляем! Ваш выигрыш: 200 000 руб. До победы осталось 4 вопроса!")
            won_now = 200000
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 200000 руб.")
            won_now = 200000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб.")
            won_now = 100000
            break

        # Вопрос №12
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

        print("\n" + quest_12)
        print("A - " + a)
        print("B - " + b)
        print("C - " + c)
        print("D - " + d)
        user_answ = input("\nВаш ответ: ")
        user_answ = user_answ.upper()
        if user_answ == answer[0] or user_answ == answer[1]:
            print("\nПоздравляем! Ваш выигрыш: 400 000 руб. До победы осталось 3 вопроса!")
            won_now = 400000
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 400000 руб.")
            won_now = 400000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Вы были близки!")
            won_now = 100000
            break

        # Вопрос №13
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

        print("\n" + quest_13)
        print("A - " + a)
        print("B - " + b)
        print("C - " + c)
        print("D - " + d)
        user_answ = input("\nВаш ответ: ")
        user_answ = user_answ.upper()
        if user_answ == answer[0] or user_answ == answer[1]:
            print("\nПоздравляем! Ваш выигрыш: 800 000 руб. До победы осталось 2 вопроса!")
            won_now = 800000
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 800000 руб.")
            won_now = 800000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Вы были очень близки!")
            won_now = 100000
            break

        # Вопрос №14
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

        print("\n" + quest_14)
        print("A - " + a)
        print("B - " + b)
        print("C - " + c)
        print("D - " + d)
        user_answ = input("\nВаш ответ: ")
        user_answ = user_answ.upper()
        if user_answ == answer[0] or user_answ == answer[1]:
            print("\nПоздравляем! Ваш выигрыш: 1 500 000 руб. До победы остался 1 вопрос!")
            won_now = 1500000
        elif user_answ == "Q":
            print("Вы решили уйти из игры, забрав с собой деньги! Ваш выигрыш: 1500000 руб.")
            won_now = 1500000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Очень жаль, ведь оставался один вопрос!")
            won_now = 100000
            break

        # Вопрос №15
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

        print("\n" + quest_15)
        print("A - " + a)
        print("B - " + b)
        print("C - " + c)
        print("D - " + d)
        user_answ = input("\nВаш ответ: ")
        user_answ = user_answ.upper()
        if user_answ == answer[0] or user_answ == answer[1]:
            print("\nПриносим свои поздравления! Вы победитель нашей игры! Вы миллионер и ваш выигрыш составляет 3 000 000 рублей!")
            won_now = 3000000
            break
        else:
            print("\nК сожалению, вы проиграли! Ваш выигрыш: 100 000 руб. Если бы вы ответили верно, то стали бы миллионером.")
            won_now = 100000
            break

    won += won_now
    print("Спасибо за игру! Вот сумма, которую вы выиграли за все игры: " + str(won) + " руб.")
    quit = input("Хотите сыграть ещё раз? (Да/Нет): ")
print("Удачи!")