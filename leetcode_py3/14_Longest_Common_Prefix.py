class Solution:
    def longestCommonPrefix(self,strs):
        strs = list(zip(*strs))
        prefix = ""
        for s in strs:
            if len(set(s)) == 1:
                prefix += set(s).pop()
            else:
                break
        return prefix

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))
    
    '''
    Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
