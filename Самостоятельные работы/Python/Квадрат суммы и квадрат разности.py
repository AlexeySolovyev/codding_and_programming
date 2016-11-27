import sys

print("Квадрат суммы и разности")

a, b = input("Введите 1-е число: "), input("Введите 2-е число: ")
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)
else:
    print("Error!")
    sys.exit()

answ_minus = (a-b)*(a-b)
answ_plus = (a+b)*(a+b)
print("(", a, "-", b, ")*(", a, "-", b, ")=", answ_minus)
print("(", a, "+", b, ")*(", a, "+", b, ")=", answ_plus)
