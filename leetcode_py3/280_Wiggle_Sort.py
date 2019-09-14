class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if i%2 == 0 and nums[i-1] < nums[i] or i%2 == 1 and nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        return nums

if __name__ == '__main__':
    nums = [3, 5, 2, 1, 6, 4]
    print(Solution().wiggleSort(nums))