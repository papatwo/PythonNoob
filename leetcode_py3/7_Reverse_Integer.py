class Solution:
    def reverse(self, x):

        if x >= 0:
            sign = 1
        elif x < 0:
            sign = -1
        
        res = 0
        x = abs(x)
        while x > 0:
            bit = x % 10
            x = x // 10
            res = res * 10 + bit
        
        res *= sign   
        if res < -2147483648 or res > 2147483647: 
            return 0
            
        return res
      
if __name__ == '__main__':
    x = 1123
    print(Solution().reverse(x)) 


'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123 Output: 321 Example 2:

Input: -123 Output: -321 Example 3:

Input: 120 Output: 21 Note: Assume we are dealing with an environment which
could only store integers within the 32-bit signed integer range: [−231,  231
− 1]. For the purpose of this problem, assume that your function returns 0
when the reversed integer overflows.

''' 
        