print("Найдите плотность (p), массу (m), объём (V), указав два известных значения")
m = input("Укажите m - массу в кг: ")
V = input("Укажите V - объём в куб. м.: ")
p = input("Укажите p - плотность в кг/куб. м.: ")

if m == "" and (p and V) != "":
    p = float(p)
    V = float(V)
    m = p * V
    print(m, " - масса объёкта.")
elif V == "" and (m and p) != "":
    m = float(m)
    p = float(p)
    V = m / p
    print(V, " - объём объёкта.")
elif p == "" and (m and V) != "":
    m = float(m)
    V = float(V)
    p = m / V
    print(p, "кг/куб. м. - плотность объёкта.")
elif ((m and V) or (m and p) or (V and p)) == "":
    print("У вас более одного неизвестного значения!")
elif (m and V and p) != "":
    print("У вас нет неизвестных значений!")
else:
    print("Error!")
