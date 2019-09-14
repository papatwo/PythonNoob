class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)+1)//2
        left, right = nums[:mid], nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]
        return nums

if __name__ == '__main__':
    nums = [1, 5, 1, 1, 6, 4]
    print(Solution().wiggleSort(nums))



'''

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2]
< nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4] Output: One possible answer is [1, 4, 1, 5,
1, 6]. Example 2:

Input: nums = [1, 3, 2, 2, 3, 1] Output: One possible answer is [2, 3, 1, 3,
1, 2]. Note: You may assume all input has valid answer.

'''