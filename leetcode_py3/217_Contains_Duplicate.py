from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums):
        check = {}
        # check = defaultdict(int)

        if nums is None:
            return False
        elif len(nums) == 1:
            return False
        else:
            for num in nums:
                if num not in check.keys():
                    check[num] = 1
                else:
                    return True
            # for num in nums:
            #     print(check[num])
            #     if check[num] == 0:
            #         check[num] += 1
            #     else:
            #         return True


if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))

''' Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1] Output: true 

Example 2:

Input: [1,2,3,4] Output: false 

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2] Output: true '''
