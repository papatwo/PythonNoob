class Solution:
    def firstMissingPositive(self, nums):
        L = len(nums)
        for i, num in enumerate(nums):
            while nums[i] > 0 and nums[i] < L and nums[i] != nums[nums[i]-1]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        # print(nums)

        for j, num in enumerate(nums):
            if num != j+1:
                return j + 1
        return L+1

if __name__ == '__main__':
    nums = [1,2,0]
    print(Solution().firstMissingPositive(nums))


''' Given an unsorted integer array, find the smallest missing positive
integer.

Example 1:

Input: [1,2,0] Output: 3 Example 2:

Input: [3,4,-1,1] Output: 2 Example 3:

Input: [7,8,9,11,12] Output: 1 Note:

Your algorithm should run in O(n) time and uses constant extra space '''
