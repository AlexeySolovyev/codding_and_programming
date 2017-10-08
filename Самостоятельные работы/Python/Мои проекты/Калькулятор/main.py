def calculate(wd, n1, n2): # wd - what_do, wc - what_calculate, a - answer, n1, n2 - numbers
	if wd == "+":
		printing = "сложение."
		answ = n1 + n2
	elif wd == "-":
		printing = "вычитание."
		answ = n1 - n2
	elif wd == "*":
		printing = "умножение."
		answ = n1 * n2
	elif wd == ":":
		printing = "деление."
		answ = n1 / n2
	else:
		printing = "ERROR!"
		answ = "ERROR!"
	
	return [printing, answ]


print("Калькулятор \nВводите по следующему образцу: \nчисло\n(+, -, *, :)\nчисло\n\nВвод данных активирован: ")

rep, repnum = "", ""
while rep != "q":
	num1 = float(input(""))
	what_do = input("")
	num2 = float(input(""))
	
	answer_list = calculate(what_do, num1, num2)

	print("\nВыполнено", answer_list[0])
	print("Ответ: ", answer_list[1])

	rep = input("\nЖелаете повторить? (q - выход): ")
	input()