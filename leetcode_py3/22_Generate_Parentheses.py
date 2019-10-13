class Solution:
    def generateParenthesis(self, n):
        return self.helper(n, n)
        
    def helper(self, left, right):
        if left == 0:
            return [')'*right]
        if left > right:
            return []
        res = ['('+ elem for elem in self.helper(left-1, right)]
        res += [')'+ elem for elem in self.helper(left, right-1)]
        return res
        

if __name__ == '__main__':
    n = 5
    print(Solution().generateParenthesis(n))


'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''    