import os           
import shutil
import sys

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
        
def main():
    print(" ")
    print(" ")
    name = input("Введите имя пользователя: ")
    print(" ")
    print("Дорогой " + name + ", спешу уведомить тебя, что ты должен сделать следующие шаги для   работоспособности программы:")
    print("Пуск =>")
    print("Все программы =>")
    print("Стандартные =>")
    print("Командная строка =>")
    print("pip install psutil")
    print("Спасибо!")
    import psutil
    print(" ")

    print("Добро пожаловать в мир Python, " + name + "!")
    answer = ""
    while answer != 'Нет':
        print(" ")
        print(" ")
        answer = input("Давай поработаем? (Да/Нет): ")

        if answer == 'Да':
            print(" ")
            print("Что ты хочешь сделать:")
            print(" [1] - вывод списка файлов;")
            print(" [2] - вывод информации о системе;")
            print(" [3] - вывод списка ИД запущенных процессов;")
            print(" [4] - дублирование файлов в текущей директории;")
            print(" [5] - удаление дубликатов в указанной директории;")

            work_user = int(input("Укажите номер действия: "))

            if work_user == 1:
                print(os.listdir())

            elif work_user == 2:
                print("Количество процессов: ",  psutil.cpu_count())
                print("Директория, в которой ты находишься: " + os.getcwd())
                print("Пользователь: " + os.getlogin())
                print("Операционная система: " + sys.platform)
                print("Кодировка системы: " + sys.getfilesystemencoding())

            elif work_user == 3:
                print(psutil.pids())

            elif work_user == 4:
                print("...Дублирование файлов...")
                file_list = os.listdir()
                i = 0
                while i < len(file_list):
                    dupl(file_list[i])
                    i += 1

            elif work_user == 5:
                print("...Удаление дубликатов...")
                print("(Для удаления из текущей директории поставьте точку.)")
                dirname = input("Укажите имя директории: ")
                file_list = os.listdir(dirname)
                for f in file_list:
                    fullname = os.path.join(dirname, f)
                    if fullname.endswith('.dupl'):
                        os.remove(fullname)
                        print("Удаление ", f, " завершено!")
                    else:
                        print(f, " - не дубликат!")

            else:
                print("Некорректный ввод!")

        elif answer == 'Нет':
            print("До скорой встречи, " + name + "!")
            input()

        else:
            print("Неккоректный ввод!")
            input()
            
if __name__ == "__main__":
    main()
