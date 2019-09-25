class Solution:
    def convertToTitle(self, n):
        if n == 0:
            return ''
        
        return self.convertToTitle((n-1)//26) + chr(ord('A') + (n-1)%26) 
        
        
        # res = ''

#         while n:
#             res += chr(ord('A') + (n - 1)%26)
#             n = (n - 1) // 26
            
#         return res[::-1]


if __name__ == '__main__':
    n = 701
    print(Solution().convertToTitle(n))


'''

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''