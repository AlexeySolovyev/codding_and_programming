import sys

print("Алгоритм Евклида для нахождения НОК")
a, b = input("Введите 1-е число: "), input("Введите 2-е число: ")
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)
else:
    print("Error!")
    sys.exit()

NOD_a, NOD_b = a, b

while NOD_a != NOD_b:
    if NOD_a > NOD_b:
        NOD_a -= NOD_b
    elif NOD_b > NOD_a:
        NOD_b -= NOD_a

NOK = (a * b) / NOD_a
print(NOK)
