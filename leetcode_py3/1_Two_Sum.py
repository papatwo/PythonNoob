class Solution(object):
	def twoSum(self, nums, target):
		temp_dict = {}
		for index, val in enumerate(nums):
			if target - val in temp_dict:
				result = [index, temp_dict[target-val]]
				return result
			temp_dict[val] = index





if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	print(Solution().twoSum(nums, target))

'''
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


