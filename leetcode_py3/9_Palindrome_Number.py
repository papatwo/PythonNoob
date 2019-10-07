class Solution:
    def isPalindrome(self, x):
        str_x = str(x)
        left, right = 0, len(str_x)-1
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome2(self, x):
        if x < 0:
            return False

        reverse = 0
        origin = x
        while x > 0:
            reverse = reverse * 10 + x % 10 # take last digit out and stack up to form reverse
            x = x // 10 # take last digit out

        if reverse == orgin:
            return True
        else:
            return False
 
if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))
    print(Solution().isPalindrome2(x))


'''

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

'''
        