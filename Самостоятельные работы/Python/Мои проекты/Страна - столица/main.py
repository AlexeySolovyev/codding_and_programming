import shelve   # Модуль shelve создаёт БД, похожую на словарь
import sys
Capitals = shelve.open("Capitals_db")   # Открываем базу; параметры: filename - имя файла (обяз.), protokol (по умол. - None) - протокол сохранения (необяз.), flag (по умол. - "c") - режим открытия

print("Привет! Здесь вы сможете узнать столицу любой страны!")
country = input("Введите название страны: ").capitalize()

if Capitals.get(country) != None:   # Получает значение по ключу, если отсутст., то возвращает дефолт; параметры: default (по умол. - None) - возвращаемое значение, при отсутст. ключа
    print("Столица вашей страны - " + Capitals[country])    # Работаем с БД, как с обычным словарём
else:
    print("К сожалению, мы не нашли столицу вашей страны...")
    print("Но вы можете добавить её сами! :)")
    want_add = input("Хотите? ").lower()
    if want_add == "нет":
        print("Печально... Тогда прощайте!")
        input()
        sys.exit()
    name_correct = input("Название страны " + country + " записано верно? ").lower()
    if name_correct == "нет":
        country = input("А как правильно? ").capitalize()
    city = input("А теперь напишите столицу твоей страны: ").capitalize()
    Capitals[country] = city
    print("Ваши страна и столица были успешно записаны в список!")
    
want_help = input("Хочешь помочь добавить новые страны и столицы? ").lower()
if want_help != "нет":
    while True:
        country = input("Введите страну: ").capitalize()
        city = input("Введите столицу: ").capitalize()
        Capitals[country] = city
        print("Успешно добавлено!")
        want_exit = input("Хочешь ещё? ").lower()
        if want_exit == "нет":
            break

if Capitals.get(country) != None:
    print("До свидания!")
else:
    print("Спасибо за улучшение нашего сервиса! \nДо свидания!")
input()

Capitals.close()