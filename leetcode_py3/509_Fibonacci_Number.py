# Recursion
# class Solution:
#     def fib(self, N: int) -> int:
#         if N== 0:
#             return 0
#         elif N== 1:
#             return 1
#         while N > 1:
#             return self.fib(N-1)+self.fib(N-2)

# Dynamic Programming
# class Solution(object):
#     def fib(self, N):
#         dic = {}
#         if N in dic:
#             return dic[N]
#         if N == 0:
#             return 0
#         elif N == 1:
#             return 1
#         elif N == 2:
#             return 1
#         else:
#             value = self.fib(N-1) + self.fib(N-2)
#         dic[N] = value
#         return value

# without recursion
class Solution:
    def fib(self, N):
        if N <= 1:
            return N     
        
        fib_results = [0,1]
        
        for i in range(2, N+1):
            fib_results.append(fib_results[i-1] + fib_results[i-2])
        
        return fib_results[N]


if __name__ == '__main__':
    N = 4
    print(Solution().fib(N))

'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
'''
        