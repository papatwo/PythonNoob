#!/usr/bin/env python

def _private_1(name): # private var
	return 'Hello, %s' % name

def _private_2(name): # private var
	return 'Hi, %s' % name

def greeting(name): # public function
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

# 调用该public函数code
# python
# import private
# private.greeting('name') 