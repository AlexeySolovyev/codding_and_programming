import shelve

reading = input("Введите имя читаемой базы: ")
try:
    db = shelve.open(reading, "w")
except Exception:
    print("ERROR! Файла не существует!")
else:
    while True:
        print("\n\nСписок действий с БД: \n[1] - очистка БД \n[2] - вывести значение по ключу \n[3] - удалить пару из БД, запросив её по ключу \n[4] - добавить запись в БД \n[5] - проверить наличие пары в БД, запросив её по ключу")
        what_want = input("Что нужно сделать? ")

        if what_want == "1":
            db.clear()
            print("Успешно очищено!")
        elif what_want == "2":
            key = input("Введите ключ: ")
            print(db.get(key, "ERROR! Ключа не существует!"))
        elif what_want == "3":
            key = input("Введите ключ: ")
            try:
                del db[key]
                print("Успешно удалено!")
            except KeyError:
                print('ERROR! Ключа не существует!')
            finally:
                input()
        elif what_want == "4":
            key = input("Введите ключ: ")
            value = input("Введите значение: ")
            db.update(key = value)
            print("Успешно добавлено!")
        elif what_want == "5":
            key = input("Введите ключ: ")
            is_has = db.has_key(key)
            if is_has:
                print("Пара " + key + " + " + db[key] + " существует.")
        else:
            print("ERROR! Команда отсутствует!")

        want_exit = input("\nХотите выйти? ").lower()
        if want_exit == "да":
            break
finally:
    db.close()
    input()
