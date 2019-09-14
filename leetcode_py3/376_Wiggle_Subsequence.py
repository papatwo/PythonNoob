class Solution:
    def wiggleMaxLength(self, nums): 
        # DP
        up, down = 1, 1
        if len(nums) < 2:
            return len(nums)
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)


        # tranverse   
#         diff_seq = []
#         max_seq = 1
#         cur_seq = 1
#         zero_count = 0
        
#         if len(nums) < 2:
#             return len(nums)
            
#         for i in range(1, len(nums)):
#             if nums[i]-nums[i-1] < 0:
#                 diff_seq.append(-1)
#             elif nums[i]-nums[i-1] > 0:
#                 diff_seq.append(1)
#             else:
#                 diff_seq.append(0)
#                 zero_count += 1
        
#         if zero_count == len(diff_seq):
#             return 1
        
#         prev = diff_seq[0]
#         for i in range(1, len(diff_seq)):
#             if diff_seq[i] * prev < 0:
#                 cur_seq += 1
#                 prev = diff_seq[i]
#             elif diff_seq[i] * prev == 0 and prev == 0:
#                 prev = diff_seq[i]
#             else:
#                 continue
#             max_seq = max(cur_seq, max_seq) 
#         return max_seq+1
        

if __name__ == '__main__':
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(Solution().wiggleMaxLength(nums))


'''

A sequence of numbers is called a wiggle sequence if the differences between
successive numbers strictly alternate between positive and negative. The first
difference (if one exists) may be either positive or negative. A sequence with
fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences
(6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5]
and [1,7,4,5,5] are not wiggle sequences, the first because its first two
differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence
that is a wiggle sequence. A subsequence is obtained by deleting some number
of elements (eventually, also zero) from the original sequence, leaving the
remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5] Output: 6 Explanation: The entire sequence is a wiggle
sequence. Example 2:

Input: [1,17,5,10,13,15,10,5,16,8] Output: 7 Explanation: There are several
subsequences that achieve this length. One is [1,17,10,13,10,16,8]. Example 3:

Input: [1,2,3,4,5,6,7,8,9] Output: 2

'''