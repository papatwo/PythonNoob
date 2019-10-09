class Solution:
    def isValid(self, s):
        close_b = {')': '(', '}': '{', ']': '['}
        
        if not s:
            return True
        
        if len(s) == 1:
            return False
        
        stack = []
        for i in s:
            if i not in close_b:
                stack.append(i)
            elif stack and close_b[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
            
        return not(stack) 

if __name__ == '__main__':
    s = "(])"
    print(Solution().isValid(s))


'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''
            
        