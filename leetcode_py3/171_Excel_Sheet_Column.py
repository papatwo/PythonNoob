class Solution:
    def titleToNumber(self, s):
        res = 0
        for c in s:
            res = 26 * res + ((ord(c) - ord('A') + 1))
        return res


if __name__ == '__main__':
    s = "ZY"
    print(Solution().titleToNumber(s))
'''

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

'''