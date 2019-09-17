class Solution:
    def isIsomorphic(self, s, t):
        
        s_dict = {}
        s_pattern = [0]*len(s)
        t_dict = {}
        t_pattern = [0]*len(t)
        
        for i, c in enumerate(s):
            if c in s_dict:
                s_pattern[i] = s_dict[c]
            else:
                s_dict[c] = i
                s_pattern[i] = s_dict[c]
             
        for i, c in enumerate(t):
            if c in t_dict:
                t_pattern[i] = t_dict[c]
            else:
                t_dict[c] = i
                t_pattern[i] = t_dict[c]
                
        # print(s_pattern)
        # print(t_pattern)
                
        return s_pattern == t_pattern


if __name__ == '__main__':
    s = "paper"
    t = "title"
    print(Solution().isIsomorphic(s, t))


'''

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add" Output: true Example 2:

Input: s = "foo", t = "bar" Output: false Example 3:

Input: s = "paper", t = "title" Output: true

'''
                