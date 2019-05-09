def inser_sort(alist):
	for j in range(1, len(alist)): # n times
		i = j
		while i > 0: # n times: worst-O(n^2) // best-O(n)
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]
				i -= 1
			else:
				break

# what if alist[i] > alist[i+1]:





if __name__ == "__main__":
	li =[54, 26, 93, 17, 77, 31, 44, 55, 20]
	print li
	inser_sort(li)
	print li