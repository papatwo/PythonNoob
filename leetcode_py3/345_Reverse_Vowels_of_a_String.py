class Solution:
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        v_idx = []
        for i, c in enumerate(s):
            if c in vowels:
                v_idx.append(i)
        
        left = 0
        right = len(v_idx) - 1
        s = list(s)
        while left <= right:
            s[v_idx[left]], s[v_idx[right]] = s[v_idx[right]], s[v_idx[left]]
            left += 1
            right -= 1
        return "".join(s)
        
        
        # left, right = 0, len(s) - 1
        # s = list(s)
        # while left < right:
        #     if s[left] not in vowels:
        #         left += 1
        #     elif s[right] not in vowels:
        #         right -= 1
        #     else:
        #         s[left], s[right] = s[right], s[left]
        #         left += 1
        #         right -= 1
        # return "".join(s)
        
if __name__ == '__main__':
    s = "leetcode"
    print(Solution().reverseVowels(s))



'''

Write a function that takes a string as input and reverse only the vowels of a
string.

Example 1:

Input: "hello" Output: "holle" Example 2:

Input: "leetcode" Output: "leotcede" Note: The vowels does not include the
letter "y".

'''
              
        