def quicksort(alist, first, last):
	if first >= last:
		return

	mid_val = alist[first]
	n = len(alist)
	high = last
	low = first

	while low < high:
		while low < high and alist[high] >= mid_val:
			high -= 1
		alist[low] = alist[high]
		# low += 1 # commen out this line to check low < high first avoid miss overlap

		while low < high and alist[low] < mid_val:
			low += 1
		alist[high] = alist[low]
		# high -= 1

	# quite while when low = high
	alist[low] = mid_val

	# quick sort left side
	quicksort(alist, first, low-1)
	# quick sort right side
	quicksort(alist, low+1, last)



if __name__ == "__main__":
	li =[54, 26, 93, 17, 77, 31, 44, 55, 20]
	print li
	quicksort(li, 0, len(li)-1)
	print li