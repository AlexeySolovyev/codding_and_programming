from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Калькулятор")


def calc(key):
    if key == "=":
        str1 = "+-/*0123456789.^"
        if calcEntry.get()[0] not in str1:
            calcEntry.insert(END, "Ошибка! Введено не число!")

        try:
            result = eval(calcEntry.get())
            calcEntry.insert(END, "=" + str(result))
        except:
            calcEntry.insert(END, "Ошибка! Проверьте правильность данных!")
    elif key == "C":
        calcEntry.delete(0, END)
    elif key == "+/-":
        if "=" in calcEntry.get():
            calcEntry.delete(0, END)

            try:
                if calcEntry.get()[0] == "-":
                    calcEntry.delete(0)
                else:
                    calcEntry.insert(0, "-")
            except IndexError:
                pass
    elif key == "<-":
        calcEntry.delete(len(calcEntry.get()) - 1)
    else:
        if "=" in calcEntry.get():
            calcEntry.delete(0, END)
        calcEntry.insert(END, key)

bttnList = [
    "<-", "C", "//", "+/-",
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/"
]

r = 1
c = 0

for bttn in bttnList:
    cmd = lambda x=bttn: calc(x)
    ttk.Button(root, text=bttn, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

calcEntry = Entry(root, width=50)
calcEntry.grid(row=0, column=0, columnspan=4)

root.mainloop()
