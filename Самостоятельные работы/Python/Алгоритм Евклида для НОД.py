print("Алгоритм Евклида для нахождения НОД")
a, b = input("Введите 1-е число: "), input("Введите 2-е число: ")
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)
else:
    print("Error!")
    exit()

while a != b:
    if a > b:
        a -= b
    elif b > a:
        b -= a

print(a)
