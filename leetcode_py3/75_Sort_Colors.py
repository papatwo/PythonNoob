class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1:
            return nums 
        
        i = 0
        left = 0
        # white = red
        right = len(nums)-1 
        
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1 
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1
        return nums
    
                
            
        
        # if len(nums) <= 1:
        #     return nums
        
#         red, white, blue = 0, 0, 0
        
#         for num in nums:
#             if num == 0:
#                 red += 1
#             elif num == 1:
#                 white += 1
#             else:
#                 blue += 1
        
#         nums[:red] = [0 for i in nums[:red]]
#         nums[red:white+red] = [1 for i in nums[red:white+red]]
#         nums[white+red:blue+white+red] = [2 for i in nums[white+red:blue+white+red]]
        
#         return nums
            
        

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    print(Solution().sortColors(nums))

'''

Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0] Output: [0,0,1,1,2,2] Follow up:

A rather straight forward solution is a two-pass algorithm using counting
sort. First, iterate the array counting number of 0's, 1's, and 2's, then
overwrite array with total number of 0's, then 1's and followed by 2's. Could
you come up with a one-pass algorithm using only constant space?

'''