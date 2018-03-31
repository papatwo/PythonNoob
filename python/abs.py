#!/usr/bin/env python
# print abs value of an int
a = 100
if a>= 0:
	print a
else:
	print -a


b = raw_input('enter an int: ') # raw_input prompt text not int
b = int(b) # convert text to int
if b >=0:
	print 'the abs value is',b
else:
	print 'the abs value is',-b


c = input('enter an int2: ') # input prompt int
if c >=0:
	print 'the abs value is',c
else:
	print 'the abs value is',-c	


