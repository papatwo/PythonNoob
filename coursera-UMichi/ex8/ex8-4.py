# https://www.py4e.com/html3/08-lists

file = open('romeo.txt')
wlist = list()
for line in file:
	line = line.rstrip()
	words = line.split()
	# print(words)
	for word in words:
		if word not in wlist:
			wlist.append(word)

wlist.sort()
print(wlist)