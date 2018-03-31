# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1) # return句含有表达式，可能造成栈溢出


a = fact(5)
print a


# 改进为尾递归函数

def fact1(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product) # 没有表达式，仅返回递归函数本身，计算是在调用前就完成的作为参数传入函数

b = fact1(5)
print b