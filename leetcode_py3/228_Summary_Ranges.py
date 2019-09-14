class Solution:
    def summaryRanges(self, nums):
        if len(nums) < 1:
            return []
        if len(nums) == 1:
            return ['%d'%nums[0]]
        
        range_list = []
        start = nums[0]
        out = []
        end= None
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] == 1:
                end = nums[i]
            else:
                range_list.append([start,end])
                start = nums[i]
                end = None
        
        range_list.append([start, end])
        
        for r in range_list:
            if r[1] is None:
                out.append('%d'%r[0])
            else:
                out.append('%d->%d'%(r[0],r[1]))
        return out



if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums))



'''

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''
            
        