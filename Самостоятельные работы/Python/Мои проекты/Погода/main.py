import bs4
import time
import requests

today, dplus = '', 0
day = time.strftime('%d')
month = time.strftime('%m')
year = time.strftime('%Y')

while today != 1 and today != 2: 
	today = int(input('На какой день вывести погоду? \n1. На сегодня \n2. На другой день (не больше, чем на неделю вперёд) \nВведите 1 или 2: '))

if today == 2:
	while True:
		day = time.strftime('%d')
		day = input('Введите день (' + str(day) + '-0' + str(int(day)+6) + '): ')
		dplus = int(day) - int(time.strftime('%d'))
		if not day.startswith('0'):
			dayofmonth = '0' + day
		if 0 < dplus < 7:
			break


s = requests.get('https://world-weather.ru/pogoda/russia/saint_petersburg/7days')
b = bs4.BeautifulSoup(s.text, "html.parser")

temp = b.select('.morning .weather-temperature')
prob = b.select('.morning .weather-probability')
hum = b.select('.morning .weather-humidity')
pres = b.select('.morning .weather-pressure')
m = temp[dplus].getText()
m_prob = prob[dplus].getText()
m_hum = hum[dplus].getText()
m_pres = pres[dplus].getText()

temp = b.select('.day .weather-temperature')
prob = b.select('.day .weather-probability')
hum = b.select('.day .weather-humidity')
pres = b.select('.day .weather-pressure')
d = temp[dplus].getText()
d_prob = prob[dplus].getText()
d_hum = hum[dplus].getText()
d_pres = pres[dplus].getText()

temp = b.select('.evening .weather-temperature')
prob = b.select('.evening .weather-probability')
hum = b.select('.evening .weather-humidity')
pres = b.select('.evening .weather-pressure')
e = temp[dplus].getText()
e_prob = prob[dplus].getText()
e_hum = hum[dplus].getText()
e_pres = pres[dplus].getText()


print('--------------------------------------------------------------------------------')
print(('ПРОГНОЗ ПОГОДЫ НА ' + day + '.' + month + '.' + year).center(80))
print('--------------------------------------------------------------------------------')
print('Утром: ' + m + 'С\nДавление: ' + m_pres + ' мм р. с.\nВероятность осадков: ' + m_prob + '\nВлажность воздуха: ' + m_hum)
print('\n\nДнём: ' + d + 'С\nДавление: ' + d_pres + ' мм р. с.\nВероятность осадков: ' + d_prob + '\nВлажность воздуха: ' + d_hum)
print('\n\nВечером: ' + e + 'С\nДавление: ' + e_pres + ' мм р. с.\nВероятность осадков: ' + e_prob + '\nВлажность воздуха: ' + e_hum)

input()
