from tkinter import *
from tkinter import messagebox


def quest1():
    question = Label(root, text="Висит груша - нельзя скушать. Что это?")
    answer = Entry()
    button = Button(root, text="Ответить", command=lambda: game(quest2))
    question.grid(row=0)
    answer.grid(row=1)
    button.grid(row=2)

    def game(qu):
        if answer.get().lower() == "лампочка" or answer.get().lower() == "лампа":
            messagebox.showinfo("Правильный ответ!", "Молодец! Ты правильно ответил на вопрос!")
            qu()
        else:
            messagebox.showerror("Неправильный ответ!", "Попробуй ещё раз!")


def quest2():
    question = Label(root, text="Зимой и летом одного цвета. Что это?")
    answer = Entry()
    button = Button(root, text="Ответить", command=lambda: game(exit))
    question.grid(row=0)
    answer.grid(row=1)
    button.grid(row=2)

    def game(qu):
        if answer.get().lower() == "ёлка" or answer.get().lower() == "ёлочка":
            messagebox.showinfo("Правильный ответ!", "Молодец! Ты правильно ответил на вопрос!")
            qu()
        else:
            messagebox.showerror("Неправильный ответ!", "Попробуй ещё раз!")


root = Tk()
root.title("Викторина")
root.geometry("225x75")

quest1()

root.mainloop()
