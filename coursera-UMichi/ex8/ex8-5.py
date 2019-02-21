# https://www.py4e.com/html3/08-lists

file = open('mail.txt')
count = 0
for line in file:
	if line.startswith('From'):
		words = line.split()
		print(words[1])
		if words[0] != 'From:':
			count += 1

print('There were', count, 'lines in the file with From as the first word')
