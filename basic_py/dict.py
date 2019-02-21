#!/usr/bin/env python

d = {'a':1, 'b':2, 'c':3} 
print d['a']

d['a'] = 10
print d['a']

print 'd' in d # method 1: check if a certain key exists 

# method 2: check if a certain key exists
print d.get('d') # return none
print d.get('d', -1) # return defined value -1
print d.get('a')

# delete a key (the same as list)
d.pop('a')