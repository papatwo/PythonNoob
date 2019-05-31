class Solution:
	def anagramMappings(self, A, B):
		# current = A.pop()
		# count = len(A)
		# idx_B = {}
		# idx_map = []

		# for i, b in enumerate(B):
		# 	print(b)
		# 	print(b==current)
		# 	if b == current:
		# 		idx_map[count] = i 
		# 		current = A.pop()
		# 		count -= 1
		# 	else:
		# 		if current in idx_B:
		# 			idx_map[count] = idx_B[current]
		# 			current = A.pop()
		# 			count -= 1
		# 		else:
		# 			idx_B[b] = i
		# return idx_map
		idx_map = []
		idx_B = {}
		for i, b in enumerate(B):
			idx_B[b] = i

		for a in A:
			idx_map.append(idx_B[a])

		return idx_map



if __name__ == '__main__':
	A = [12, 28, 46, 32, 50]
	B = [50, 12, 32, 46, 28]

	print(Solution().anagramMappings(A, B))


''' Given two lists A and B, and B is an anagram of A. B is an anagram of A
means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the
ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers,
output any of them.

For example, given

A = [12, 28, 46, 32, 50] B = [50, 12, 32, 46, 28]
 

We should return

[1, 4, 3, 2, 0] as P[0] = 1 because the 0th element of A appears at B[1], and
P[1] = 4 because the 1st element of Aappears at B[4], and so on.

 

Note:

A, B have equal lengths in range [1, 100]. A[i], B[i] are integers in range
[0, 10^5]. '''
