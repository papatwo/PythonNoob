# https://www.py4e.com/html3/09-dictionaries

file = open('mail.txt')
sent = dict()
for line in file:
	if line.startswith('From'):
		words = line.split()
		if len(words) > 2:
			sent[words[1]] = sent.get(words[1], 0) + 1

print(sent)

