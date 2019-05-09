def mergesort(alist):

	n = len(alist)
	if n <= 1:
		return alist
	mid = n / 2

	# left/right is sorted sublist after merge sort
	left = mergesort(alist[:mid])
	right = mergesort(alist[mid:])
	# merge sorted sublist to a new one
	left_pointer, right_pointer = 0, 0
	merge = []

	while left_pointer < len(left) and right_pointer < len(right):
		if left[left_pointer] < right[right_pointer]:
			merge.append(left[left_pointer])
			left_pointer += 1
		elif left[left_pointer] > right[right_pointer]:
			merge.append(right[right_pointer])
			right_pointer += 1

	merge += left[left_pointer:]
	merge += right[right_pointer:]

	return merge


if __name__ == "__main__":
	li =[54, 26, 93, 17, 77, 31, 44, 55, 20]
	print li
	sorted_li = mergesort(li)
	print sorted_li