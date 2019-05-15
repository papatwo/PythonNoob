class Solution:
	def sortedSquares(self, A: List[int]) -> List[int]:
        # return sorted([x**2 for x in A])
        
		res = []
		l, r = 0, len(A)-1
		while l<=r:
			left, right = abs(A[l]), abs(A[r])
			if left < right:
				res.append(right**2)
				r -= 1
			else:
				res.append(left**2)
				l += 1
		return res[::-1]





if __name__ == '__main__':
	A = [-4,-1,0,3,10]
	print(Solution().sortedSquares(A))

'''
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''


