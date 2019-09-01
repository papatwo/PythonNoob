class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        temp_sum = 0
        max_sum = [None] * len(nums)
        max_sum[0] = nums[0]

        for i in range(1, len(nums)):
            if max_sum[i-1] < 0:
                max_sum[i] = nums[i]

            else:
                max_sum[i] = max_sum[i-1] + nums[i] 

                
        return max(max_sum)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))

''' 
Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4], Output: 6 Explanation: [4,-1,2,1] has the
largest sum = 6. Follow up:

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle. 
'''
        