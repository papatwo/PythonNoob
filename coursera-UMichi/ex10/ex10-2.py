# https://www.py4e.com/html3/10-tuples

file = open('mail.txt')
hours = dict()
hourcnt = list()
for line in file:
	if line.startswith('From'):
		words = line.split()
		if len(words) > 2:
			time = words[5].split(':')
			hours[float(time[0])] = hours.get(float(time[0]), 0) + 1

for k, v in hours.items():
	hourcnt.append((k, v))

hourcnt_sort = sorted(hourcnt)
for k,v in hourcnt_sort:
	print('1', k,v)



# one line code by list comprehension
hourcnt_sort2 = sorted([(k,v) for k, v in hours.items()])
for k,v in hourcnt_sort2:
	print('2', k,v)

