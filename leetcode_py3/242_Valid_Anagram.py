class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        lookup = {}
        
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
      
        for i in t:
            if i in lookup:
                lookup[i] -= 1
            else:
                return False
            
        for key in lookup:
            if lookup[key] != 0:
                return False

        return True
        
        
if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))


'''

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

'''