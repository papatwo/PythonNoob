class Solution(object):
    def maxSubArrayLen(self, nums, k):
        sums = {}
        cur_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum == k:
                max_len = i + 1
            elif cur_sum - k in sums:
                max_len = max(max_len, i - sums[cur_sum-k])
            else:
                sums[cur_sum] = i 
        return max_len



if __name__ == '__main__':
     nums1 = [1, -1, 5, -2, 3]
     k1 = 3
     nums2 = [-2, -1, 2, 1]
     k2 = 1

     print(Solution().maxSubArrayLen(nums1,k1))  
     print(Solution().maxSubArrayLen(nums2,k2))   

''' 
Given an array nums and a target value k, find the maximum length of a
subarray that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3, return 4. (because the subarray [1, -1,
5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1, return 2. (because the subarray [-1, 2]
sums to 1 and is the longest)

Follow Up: Can you do it in O(n) time? 
'''
