# https://www.py4e.com/html3/09-dictionaries

file = open('mail.txt')
day = dict()
for line in file:
	if line.startswith('From'):
		words = line.split()
		if len(words) > 2:
			day[words[2]] = day.get(words[2], 0) + 1

print(day)
