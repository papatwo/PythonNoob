class Solution:
    def increasingTriplet(self, nums):
        min1 = float('inf')
        min2 = float('inf')
        if len(nums) <= 2:
            return False
        
        for num in nums:
            if num > min2:
                return True
            if num < min1:
                min1 = num
            elif num > min1 and num < min2:
                min2 = num
        return False

            
        
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(Solution().increasingTriplet(nums))



''' 
Given an unsorted array return whether an increasing subsequence of length
3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k  such that arr[i] < arr[j] < arr[k] given
0 ≤ i < j < k ≤ n-1 else return false. Note: Your algorithm should run in O(n)
time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5] Output: true Example 2:

Input: [5,4,3,2,1] Output: false 
'''
