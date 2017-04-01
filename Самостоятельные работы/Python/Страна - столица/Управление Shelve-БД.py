import shelve

reading = input("Введите имя читаемой базы: ")
try:
	db = shelve.open(reading, flag = "w")
except Exception:
	print("Файла не существует!")
else:
	while True:
	    print("\n\nСписок действий с БД: \n[1] - очистка БД \n[2] - вывести значение по ключу \n[3] - вывести значение по ключу, удалив эту пару из БД \n[4] - добавить запись в БД \n")
	    what_want = input("Что нужно сделать? ")
	    
	    if what_want == "1":
	        db.clear()
	        print("Успешно очищено!")
	    elif what_want == "2":
	        key = input("Введите ключ: ")
	        print(db.get(key, default = "Ключа не существует!"))
	    elif what_want == "3":
	        key = input("Введите ключ: ")
	        print(db.pop(key, default = "Ключа не существует!"))
	    elif what_want == "4":
	        key = input("Введите ключ: ")
	        value = input("Введите значение: ")
	        db.update(key = value)
	        print("Успешно добавлено!")
	    else:
	        print("ERROR!")
	    
	    want_exit = input("\nХотите выйти? ").lower()
	    if want_exit == "да":
	        break

	db.close()
	input()