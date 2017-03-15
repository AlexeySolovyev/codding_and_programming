import sys

Capitals_f = open("Capitals.txt", "a")
Capitals = dict()
print("Привет! Здесь ты сможешь узнать столицу любой страны!")
country = input("Введи название страны: ").capitalize()
if country in Capitals:
    print("Столица твоей страны - " + Capitlas[country])
else:
    print("К сожалению, мы не нашли столицу твоей страны...")
    print("Но ты можешь добавить её сам! :)")
    want_add = input("Хочешь? ").lower()
    if want_add == "нет":
        print("Печально... Тогда прощай!")
        input()
        sys.exit()
    name_correct = input("Название страны " + country + " записано верно? ").lower()
    if name_correct == "нет":
        country = input("А как правильно? ").capitalize()
    city = input("А теперь напиши столицу твоей страны: ").capitalize()
    Capitals_f.write(country + " - " + city + "\n")
    print("Твои страна и столица были успешно записаны в список!")

input()
Capitals_f.close()
