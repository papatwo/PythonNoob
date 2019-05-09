# O(n^2)
def bubble_sort(alist): 
	n = len(alist)
	for j in range(n-1): # n times
		for i in range(0, n-1-j): # n times
			# scan from beginning to the end 
			if alist[i]>alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]


def bubble_sort2(alist):
	n = len(alist)
	while n != 0:
		for i in range(n-1):
			# scan from beginning to the end 
			if alist[i]>alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]
		n-=1

def bubble_sort3(alist):
	n = len(alist)
	for j in range(len(alist), 0, -1):
		for i in range(0, n-1-j):
			# scan from beginning to the end 
			if alist[i]>alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]

# Optimized
def bubble_sort2(alist):
	n = len(alist)
	count = 0
	while n != 0:
		for i in range(n-1):
			# scan from beginning to the end 
			if alist[i]>alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]
				count += 1
		n -= 1
		if count == 0: # if in order, quit directly
			return


if __name__ == "__main__":
	li =[54, 26, 93, 17, 77, 31, 44, 55, 20]
	li2 = [1, 2, 3, 4, 5, 6, 7]
	print li
	bubble_sort(li)
	print li
	bubble_sort2(li)
	bubble_sort2(li2)
	print li
	print li2