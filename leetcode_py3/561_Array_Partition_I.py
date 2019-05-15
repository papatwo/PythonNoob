class Solution:
	def arrayPairSum(self, nums):
		sort_list = sorted(nums)	
		# n = len(nums) // 2
		# return sum([min(sort_list[i*2],sort_list[i*2+1]) for i in range(n)])
		return sum(sort_list[::2])


if __name__ == '__main__':
	nums = [1, 4, 3, 2]
	print(Solution().arrayPairSum(nums))


'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) 
for all i from 1 to n as large as possible.

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
'''

        