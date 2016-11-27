print("Разность квадратов.")

a, b = input("Введите 1-е число: "), input("Введите 2-е число: ")
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)
else:
    print("Error!")
    sys.exit()

answ = (a+b)*(a-b)
print("(", a, "+", b, ")*(", a, "-", b, ")=", answ)
