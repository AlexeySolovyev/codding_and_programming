from tkinter import *
from tkinter import messagebox
import shelve


def logOrPass():
    buttonToRegistration = Button(text="Регистрация", command=lambda: mainWindow.destroy() + register())
    buttonToLoginigng = Button(text="Вход", command=lambda:  mainWindow.destroy() + logining())

    buttonToLoginigng.place(x=0)
    buttonToRegistration.place(x=45)


def register():
    text = Label(text="Для входа в систему зарегестрируйтесь!")
    textLogin = Label(text="Введите логин: ")
    regLogin = Entry()
    textPass1 = Label(text="Введите пароль: ")
    regPassword1 = Entry(show="•")
    textPass2 = Label(text="Повторите пароль: ")
    regPassword2 = Entry(show="•")
    buttonReg = Button(text="Зарегестрироваться", command=lambda: saveData())

    text.grid(row=0, columnspan=2)
    textLogin.grid(row=1, column=0)
    regLogin.grid(row=1, column=1)
    textPass1.grid(row=2, column=0)
    regPassword1.grid(row=2, column=1)
    textPass2.grid(row=3, column=0)
    regPassword2.grid(row=3, column=1)
    buttonReg.grid(row=4, columnspan=2)

    def saveData():
        if regPassword1 != regPassword2:
            messagebox.showwarning("Ошибка!", "Пароли не идентичны")
        else:
            LogNPass = shelve.open("C:/logins_db")
            LogNPass[regLogin.get()] = regPassword1.get()
            messagebox.showinfo("Поздравляем!", "Вы успешно зарегестрировались! Перезапустите программу, чтобы вернуться в главное меню. С этого момента нажимайте только «Вход».")
            LogNPass.close()


def logining():
    text = Label(text="Войдите в систему!")
    textLogin = Label(text="Введите логин: ")
    logLogin = Entry()
    textPass = Label(text="Введите пароль: ")
    logPassword = Entry(show="•")
    buttonLog = Button(text="Войти", command=lambda: syncData())

    text.grid(row=0, columnspan=2)
    textLogin.grid(row=1, column=0)
    logLogin.grid(row=1, column=1)
    textPass.grid(row=2, column=0)
    logPassword.grid(row=2, column=1)
    buttonLog.grid(row=3, columnspan=2)

    def syncData():
        LogNPass = shelve.open("C:/logins_db")
        if logLogin.get() in LogNPass:
            if logPassword.get() == LogNPass[logLogin.get()]:
                messagebox.showinfo("Новые сообщения! (5)", "Добрый день! У вас 5 новых сообщений!")
            else:
                messagebox.showerror("Ошибка!", "Не совпадает пара логина и пароля!")
        else:
            messagebox.showerror("Ошибка!", "Такого логина не зарегистрировано!")
        LogNPass.close()


mainWindow = Tk()
mainWindow.geometry("125x25")

logOrPass()

mainWindow.mainloop()

root = Tk()
root.title("Вход в систему")
root.geometry("300x175")

