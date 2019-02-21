def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type') # Check the variable type
	if x >= 0:
		return x
	else:
		return -x

a = my_abs(-9)
print a

