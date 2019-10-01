class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_len = 0
        appear_table = {}
        
        
        if not s:
            return 0
        
        for ch in s:
            appear_table[ch] = None
        
        for cur in range(len(s)):
            if appear_table[s[cur]] == None:
                appear_table[s[cur]] = cur 
            else:
                start = max(start, appear_table[s[cur]]+1)
                appear_table[s[cur]] = cur
            
            max_len = max(max_len, cur-start+1)
        return max_len


if __name__ == '__main__':
    s = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(s))


    '''

    Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''