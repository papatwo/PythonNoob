#!/usr/bin/env python

classmates = ['a', 'b', 'c']
print classmates

print len (classmates) 
print classmates[0] # index starts from 0
print classmates[-1] # minus sign starts from the end

classmates.append('d') # append elements to the end
print classmates

classmates.insert(1, 'a1') # insert new element to assigned position
print classmates

classmates.pop() # delete the last element
print classmates

classmates.pop(1) # delete required element by giving its index
print classmates