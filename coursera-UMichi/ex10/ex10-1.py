# https://www.py4e.com/html3/10-tuples

file = open('mail.txt')
mail = dict()
email = list()
for line in file:
	if line.startswith('From'):
		words = line.split()
		if len(words) > 2:
			mail[words[1]] = mail.get(words[1], 0) + 1

for k, v in mail.items():
	email.append((v, k))

email_sort = sorted(email, reverse = True)
print(email_sort[0])

# one line code by list comprehension
email_sort2 = sorted([(v, k) for k, v in mail.items()], reverse = True)
print(email_sort2[0])

