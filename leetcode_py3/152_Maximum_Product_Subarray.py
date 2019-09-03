class Solution:
    def maxProduct(self, nums):
        cur_max = nums[0]
        cur_min = nums[0]
        product = nums[0]
        
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        for i in range(1, len(nums)):
            next_max = cur_max * nums[i]
            next_min = cur_min * nums[i]
            cur_max = max(next_max, next_min, nums[i])
            cur_min = min(next_max, next_min, nums[i]) 
            product = max(cur_max, product)
        return product

if __name__ == '__main__':
    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))

'''

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4] Output: 6 Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1] Output: 0 Explanation: The result cannot be 2, because
[-2,-1] is not a subarray.

'''