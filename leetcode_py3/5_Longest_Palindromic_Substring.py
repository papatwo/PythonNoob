class Solution:
    def longestPalindrome(self, s):
   
        if not s or not s.strip():
            return s
        
        palin = ""
        
        for i in range(len(s)):
            odd_len = len(self.ifpalin(s, i, i))
            if odd_len > len(palin):
                palin = self.ifpalin(s, i, i)
                
            even_len = len(self.ifpalin(s, i, i+1))
            if even_len > len(palin):
                palin = self.ifpalin(s, i, i+1)
        return palin
                
            
    
    def ifpalin(self, s, start, end):
        while start >= 0 and end < len(s) and s[start]==s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
            
        

if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))


'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''
        
        
        
        