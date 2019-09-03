class Solution:
    def minSubArrayLen(self, s, nums):
        l, r, cur_sum = 0, 0, 0
        min_len = float('Inf')
    

        for i, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= s:
                min_len = min(min_len, r-l+1)
                cur_sum -= nums[l]
                l+=1
            r+=1

        return min_len if min_len != float('Inf') else 0


if __name__ == '__main__':
    s = 7
    nums = [2,3,1,2,4,3]

    print(Solution().minSubArrayLen(s, nums))


''' 
Given an array of n positive integers and a positive integer s, find the
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3] Output: 2 Explanation: the subarray [4,3]
has the minimal length under the problem constraint. Follow up: If you have
figured out the O(n) solution, try coding another solution of which the time
complexity is O(n log n). 
'''
