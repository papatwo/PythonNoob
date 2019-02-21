# capitalise 1st letter by map


s = ['adam', 'LISA', 'barT']

ss = map(str.title, s)

print(ss)

def prod(n):
	return reduce(lambda x, y: x * y, n)

print(prod([1, 2, 3, 4, 5]))


def prime_num(num):
	if num == 1 or num == 2 or num == 3:
		return False 
	else:
		for n in range(2, num):
			if num % n == 0:
				return True

print filter(prime_num, range(1,10))
#filter() keeps every passed-in function as elements in order. If return value is 0, False, None,
#empty str, empty list, empty yuanzu, empty dict then discard, otherwise kept.
