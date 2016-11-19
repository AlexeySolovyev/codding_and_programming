def dupl(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
    if os.path.exists(newfile):
        print("Файл ", newfile, " был успешно создан!")
        return True
    else:
        print("Возникли проблемы с копированием файла ", newfile, "!")
        return False

print(" [1] - дублирование файлов в текущей дериктории;")
print(" [2] - удаление дубликатов из указанной директории;")
work_user = int(input("Укажите номер действия:"))    
    
elif work_user == 2:
    print("...Удаление дубликатов...")
    dirname = input("Укажите имя директории:")
    file_list = os.listdir(dirname)
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            print("Удаление ", f, " завершено!")
        else:
            print(f, " - не дубликат!")

            
elif work_user == 1:
    print("...Дублирование файлов...")
    file_list = os.listdir()
    i = 0
    while i < len(file_list):
        dupl(file_list[i])
        i += 1