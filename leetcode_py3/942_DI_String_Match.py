class Solution(object):
    def fast_diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        end = len(S)
        head = 0
        for s in S:
            if s =='I':
                res.append(head)
                head += 1
            else:
                res.append(end)
                end -= 1
        res.append(head)
        return res

    def my_diStringMatch(self, S):
        if not S:
            return
        else:
            N = len(S)
            N_lst = []
            output = []

            for i in range(N+1):
                N_lst.append(i)
            for s in S:
                if s == 'I':
                    output.append(N_lst.pop(0))
                elif s == 'D':
                    output.append(N_lst.pop())
            output.append(N_lst.pop())
            return output


if __name__ == '__main__':
    S = "IDID"
    print(Solution().fast_diStringMatch(S))
    print(Solution().my_diStringMatch(S))

'''

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]

'''    
