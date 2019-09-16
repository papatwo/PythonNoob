class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        if needle not in haystack:
            return -1
        else:
            for i, ch in enumerate(haystack):
                if haystack[i:i+len(needle)] == needle:
                    return i
                
if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    print(Solution().strStr(haystack, needle))


'''

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll" Output: 2 Example 2:

Input: haystack = "aaaaa", needle = "bba" Output: -1

'''