# https://www.py4e.com/html3/08-lists

numlst = list()
while True:
	num = input('enter a number: ')
	if num == 'done':
		break
	else:
		numlst.append(float(num))

print('maximum: ', max(numlst))
print('minimum: ', min(numlst))
