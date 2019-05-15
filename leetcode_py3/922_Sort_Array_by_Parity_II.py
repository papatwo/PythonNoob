class Solution:
	def sortArrayByParityII(self, A):
		if len(A) <= 1:
			return A
		else:
			res = []
			even = []
			odd = []
			for x in A:
				if x%2 == 0:
					even.append(x)
				else:
					odd.append(x)

			while even:
				res.append(even.pop())
				res.append(odd.pop())
		return res


if __name__ == '__main__':
	A = [1,4,4,3,0,3]
	print(Solution().sortArrayByParityII(A))


'''
Given an array A of non-negative integers, half of the integers in A are odd, 
and half of the integers are even.
Sort the array so that whenever A[i] is odd, 
i is odd; and whenever A[i] is even, i is even.

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

