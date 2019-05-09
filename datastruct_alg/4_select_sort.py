

def select_sort(alist):
	
	n = len(alist)
	for j in range(n-1):
		min_i = j
		for i in range(j+1, n):
			if alist[min_i] > alist[i]:
				min_i = i
		alist[min_i], alist[j] = alist[j], alist[min_i]


if __name__ == "__main__":
	li =[54, 26, 93, 17, 77, 31, 44, 55, 20]
	print li
	select_sort(li)
	print li