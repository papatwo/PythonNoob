class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        zero = len(nums) 
        
        for i, num in enumerate(nums):
            if num != 0:
                nums[cur] = num
                cur += 1
        
        nums[cur:] = [0 for i in range(zero-cur)]
        return nums
                
        
        # while cur <= zero:
        #     if nums[cur] == 0:
        #         nums[cur], nums[zero] = nums[zero], nums[cur]
        #         zero -= 1
        #         # cur += 1
        #     if nums[cur] < nums[left] and nums[cur] != 0:
        #         nums[left], nums[cur] = nums[cur], nums[left]
        #         left += 1
        #     cur += 1
        # return nums
                

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(Solution().moveZeroes(nums))


'''

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12] Output: [1,3,12,0,0] Note:

You must do this in-place without making a copy of the array. Minimize the
total number of operations.

'''

