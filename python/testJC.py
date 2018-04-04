#!/usr/bin/env python

a = [54,16,24]
b = []

if a[0] < a[1] and a[0] < a[2]:
	b.append(a[0])
	if a[1] < a[2]:
		b.append(a[1])
		b.append(a[2])
	else:
		b.append(a[2])
		b.append(a[1])
elif a[0] < a[1] and a[0] > a[2]:
	b.append(a[2])
	b.append(a[0])
	b.append(a[1])
elif a[0] > a[1] and a[0] > a[2]:
	if a[1] < a[2]:
		b.append(a[1])
		b.append(a[2])
	else:
		b.append(a[2])
		b.append(a[1])
	b.append(a[0])
else:
	b.append(a[1])
	b.append(a[0])
	b.append(a[2])

print b

