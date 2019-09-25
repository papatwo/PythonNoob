class Solution:
    def isStrobogrammatic(self, num):
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        for i in range(len(num)//2):
            if num[i] not in lookup or lookup[num[i]] !=  num[len(num)-1-i]:
                return False
        return True

if __name__ == '__main__':
    num = '123'
    print(Solution().isStrobogrammatic(num))


'''

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

Example 1:

Input:  "69" Output: true Example 2:

Input:  "88" Output: true Example 3:

Input:  "962" Output: false

'''