# https://www.py4e.com/html3/09-dictionaries

file = open('mail.txt')
maildomain = dict()
for line in file:
	if line.startswith('From'):
		words = line.split()
		if len(words) > 2:
			domain = words[1].split('@')
			maildomain[domain[1]] = maildomain.get(domain[1], 0) + 1

# bigcount = None
# bigdomain = None
# for key,val in maildomain.items():
# 	if bigcount == None or bigcount < val:
# 		bigdomain = key
# 		bigcount = val

print(maildomain)
print(bigdomain, bigcount)
