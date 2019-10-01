class Solution:
    def longestSubstring(self, s, k):
        if not s:
            return 0
        
        check = [0] * 26
        for c in s:
            check[ord(c)-ord('a')] +=1
                  
        full = True
        for i in range(len(s)):
            if check[ord(s[i])-ord('a')]>0 and check[ord(s[i])-ord('a')]<k:
                full = False
        
        if full:
            return len(s)
        
        begin, end, result = 0, 0, 0
        while end < len(s):
            if check[ord(s[end])-ord('a')] != 0 and check[ord(s[end])-ord('a')] <k:
                result = max(result, self.longestSubstring(s[begin:end],k))
                begin = end + 1
            end += 1
        
        result = max(result, self.longestSubstring(s[begin:],k))
        
        return result

#         for i,c in enumerate(check):
#             if c not in check:
#                 check[c] = 1
#             else:
#                 check[c] += 1
#                 if check[c]  k:
#                     max_len = max(max_len, left-i-1)
#                     left = i
#                     check[c] = 0
#                 else:
#                     check[c] += 1
#         return max_len
                    
                    
                
            
if __name__ == '__main__':
    s = 'ababbc'
    k = 2
    print(Solution().longestSubstring(s,k))




'''

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

'''