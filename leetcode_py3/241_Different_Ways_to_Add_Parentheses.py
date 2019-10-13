class Solution:
    def diffWaysToCompute(self, in_str):
        res = []
        for i in range(len(in_str)):
            if self.isOperator(in_str[i]):
                left = self.diffWaysToCompute(in_str[:i])
                right = self.diffWaysToCompute(in_str[i+1:])
                for l in left:
                    for r in right:
                        res.append(self.cal(l, r, in_str[i]))
        if not res:
            res.append(int(in_str))
        
        return res
        
    def isOperator(self, char):
        return char in ['+', '-', '*']
    
    def cal(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        else:
            return a * b
    

        
if __name__ == '__main__':
    in_str = "2*3-4*5"
    print(Solution().diffWaysToCompute(in_str))


'''

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

'''