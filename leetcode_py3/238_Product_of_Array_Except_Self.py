class Solution:
    def productExceptSelf(self, nums):
        # O(1) 
        cur_p = 1
        res = []
        # left
        for i in range(1,len(nums)):
            res.append(cur_p)
            cur_p *= nums[i-1]
        res.append(cur_p)
        
        cur_p = 1
        for i in range(len(nums)-2,-1,-1):
            res[i+1] *= cur_p
            cur_p *= nums[i+1]
        res[0] *= (cur_p)
        
        return res
            
        # O(n)    
        
#         left_p, right_p = [0] * len(nums), [0] * len(nums)
#         left_p[0], right_p[-1] = 1, 1
        
#         cur_p = 1
#         for i in range(1, len(nums)):
#             left_p[i] = cur_p*nums[i-1] 
#             cur_p = left_p[i]
        
#         cur_p = 1
#         for i in range(1, len(nums)):
#             right_p[-i-1] = cur_p*nums[-i]
#             cur_p = right_p[-i-1]
            
#         print(left_p)
#         print(right_p)
#         return [x*y for x, y in zip(left_p, right_p)]


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))


''' 
Given an array nums of n integers where n > 1,  return an array output
such that output[i] is equal to the product of all the elements of nums except
nums[i].

Example:

Input:  [1,2,3,4] Output: [24,12,8,6] Note: Please solve it without division
and in O(n).

Follow up: Could you solve it with constant space complexity? (The output
array does not count as extra space for the purpose of space complexity
analysis.)

'''