class Solution:
    def wordPattern(self, pattern, str):
        str = str.split()
        pattern = list(pattern)
        pattern_dict = {}
        pattern_map = [0] * len(pattern)
        str_dict = {}
        str_map = [0] * len(str)
        
        for i, c in enumerate(pattern):
            if c in pattern_dict:
                pattern_map[i] = pattern_dict[c]
            else:
                pattern_dict[c] = i
                pattern_map[i] = pattern_dict[c]
                
        for i, c in enumerate(str):
            if c in str_dict:
                str_map[i] = str_dict[c]
            else:
                str_dict[c] = i
                str_map[i] = str_dict[c]
        
        # print(str_map)
        # print(str_dict)
        # print(pattern_map)
        # print(pattern_dict)
        return str_map == pattern_map
                
                
if __name__ == '__main__':
    
    pattern = "abba"
    str = "dog cat cat dog"
    print(Solution().wordPattern(pattern, str))

'''

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog" Output: true Example 2:

Input:pattern = "abba", str = "dog cat cat fish" Output: false Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog" Output: false Example 4:

Input: pattern = "abba", str = "dog dog dog dog" Output: false

'''       