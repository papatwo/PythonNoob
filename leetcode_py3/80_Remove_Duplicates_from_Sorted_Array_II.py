class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums) == 0:
            return 0 
        j = 0
        for i in range(1,len(nums)):
            if i < 2 or nums[i] != nums[j-1]:
                nums[j+1] = nums[i]
                j += 1
        print(nums[:j+1])
        return j+1

# N.B use while loop is easier!!!               
        
#         j = 0
#         c = 1
#         for i in range(1,len(nums)):
#             if nums[j] == nums[i]:
#                 if c < 2:
#                     nums[j+1] = nums[i]
#                     c += 1
#                     j += 1
            
#             elif nums[j] != nums[i]:
#                 nums[j+1] = nums[i]
#                 j += 1
#                 c = 1
#         return j+1

if __name__ == '__main__':
        nums = [1,1,1,2,2,3]
        print(Solution().removeDuplicates(nums))  


''' Given a sorted array nums, remove the duplicates in-place such that
duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length. Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums
being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length. '''
