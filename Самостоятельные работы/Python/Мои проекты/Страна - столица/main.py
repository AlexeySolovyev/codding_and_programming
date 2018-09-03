try:
    f = open("Capitals_db.txt", 'r+')
except Exception:
    f = open("Capitals_db.txt")

Capitals = {}
lines = ''

while True:
    con = f.readline().strip()
    if not con:
        break
    cap = f.readline().strip()
    Capitals[con] = cap


print("Привет! Здесь вы сможете узнать столицу любой страны!")
country = input("Введите название страны: ")

if country in Capitals:
    print("Столица - " + Capitals[country])
else:
    print("К сожалению, мы не нашли столицу этой страны...")
    print("Но вы можете добавить её сами! :)")
    want_add = input("Хотите? ").lower()
    if want_add in ['нет', 'н', 'n', 'no']:
        exit()
    capital = input("Напишите столицу страны: ")
    f.writelines('\n' + country + '\n' + capital)
    print("Страна и её столица были успешно занесены в базу данных!")

input()
f.close()