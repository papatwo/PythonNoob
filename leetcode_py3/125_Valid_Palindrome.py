class Solution:
    def isPalindrome(self, s):
        if not s:
            return True
        
        strlist = ''
        for c in s:
            # if c.isalpha() or c.isdigit():
            if c.isalnum():
                strlist += c.lower()
 
        left, right = 0, len(strlist)-1
        while left < right:
            if strlist[left] != strlist[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))


'''

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''