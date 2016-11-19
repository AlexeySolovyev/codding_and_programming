print("Калькулятор")
print("")

rep = ""
while rep != "q":
	num1 = float(input("1-е число: "))
	num2 = float(input("2-е число: "))

	repnum = ""
	while repnum != "n":

		print("")
		what_do = input("Что сделать? (+/-/*/:/pi): ")

		if what_do == "+":
			printing = "Калькулятор производит сложение 2-х чисел!"
			answ = num1 + num2


		elif what_do == "-":
			printing = "Калькулятор производит вычитание из 1-го числа 2-е!"
			answ = num1 - num2


		elif what_do == "*":
			printing = "Калькулятор производит умножение 2-х чисел!"
			answ = num1 * num2


		elif what_do == ":":
			printing = "Калькулятор производит деление 1-го числа на 2-е!"
			answ = num1 / num2


		elif what_do == "pi" or "Pi":

			pi_rep = ""
			print("")
			print('Раздел - "операции с числом Pi"')
			while pi_rep != "n":

				pi_what_num = input("Какое число использовать для операций с числом Pi? (1/2): ")

				if pi_what_num == "1":

					print("")
					print("Выбрано число ", num1)
					print("")
					pi_what_do = input("Что сделать? (+/-/*/:): ")

					if pi_what_do == "+":
						printing = "Калькулятор производит сложение 1-го числа и числа Pi!"
						answ = num1 + 3.1415926535

					elif pi_what_do == "-":
						printing = "Калькулятор производит вычитание из 1-го числа число Pi!"
						answ = num1 - 3.1415926535
					elif pi_what_do == "*":

						printing = "Калькулятор производит умножение 1-го числа на число Pi!"
						answ = num1 * 3.1415926535
					elif pi_what_do == ":":
						printing = "Калькулятор производит деление 1-го числа на число Pi!"
						answ = num1 / 3.1415926535
					else:
					    printing = "ERROR!"
					    answ = "ERROR!"


				elif pi_what_num == "2":

					print("")
					print("Выбрано число ", num2)
					print("")
					pi_what_do = input("Что сделать? (+/-/*/:): ")

					if pi_what_do == "+":
						printing = "Калькулятор производит сложение 2-го числа и числа Pi!"
						answ = num2 + 3.1415926535

					elif pi_what_do == "-":
						printing = "Калькулятор производит вычитание из 2-го числа число Pi!"
						answ = num2 - 3.1415926535

					elif pi_what_do == "*":
						printing = "Калькулятор производит умножение 2-го числа на число Pi!"
						answ = num2 * 3.1415926535

					elif pi_what_do == ":":
						printing = "Калькулятор производит деление 2-го числа на число Pi!"
						answ = num2 / 3.1415926535

					else:
					    printing = "ERROR!"
					    answ = "ERROR!"


				else:
				    printing = "ERROR!"
				    answ = "ERROR!"

				pi_rep = input("Повторить операции с числом Pi? (n - нет): ")


		else:
		    printing = "ERROR!"
		    answ = "ERROR!"

		print("")
		print("Выполнено: ", printing)
		print("Ответ: ", answ)
		print("")

		repnum = input("Повторить операции с этими числами ещё раз? (n - нет): ")
		print("")

	rep = input("Повторить операции с другими числами? (q - выход): ")
