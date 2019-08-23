class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary find
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left+(right-left)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
                
            if count <= mid:
                left = mid+1 
            else:
                right = mid
        return right
        
        #linked circle
#         slow = nums[0]
#         fast = nums[nums[0]]
#         while slow != fast:
#             fast = nums[nums[fast]]
#             slow = nums[slow]
        
#         fast = 0
#         while slow != fast:
#             fast = nums[fast]
#             slow = nums[slow]
#         return fast
        
          # dictionary
#         num_dict = {}
#         for num in nums:
#             if num not in num_dict:
#                 num_dict[num] = 1
#             else:
#                 num_dict[num] += 1
                
#         for key in num_dict:
#             if num_dict[key] > 1:
#                 return key

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(Solution().findDuplicate(nums))

''' 
Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive), prove that at least one duplicate number must
exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2] Output: 2 Example 2:

Input: [3,1,3,4,2] Output: 3 Note:

You must not modify the array (assume the array is read only). You must use
only constant, O(1) extra space. Your runtime complexity should be less than
O(n2). There is only one duplicate number in the array, but it could be
repeated more than once.
'''

        