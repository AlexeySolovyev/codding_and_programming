count = int((open('input.txt', 'r')).read())
if (100 % (count*2) > 0):
	int((open('output.txt', 'w'))).write((100 // (count*2)) + 1)
else:
	int((open('output.txt', 'w')).read()).write(100 // (count*2))