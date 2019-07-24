
class Solution:
    def hIndex(self, citations):
        h = 0
        num_paper = len(citations)
        
        citations = sorted(citations, reverse=True)
        
        for i, cite in enumerate(citations):
            if i+1 <= cite:
                h = i+1
        return h
                
        # [6, 5, 3, 1, 0]
        # [7, 4, 6, 2, 4]
        # [2, 4, 4, 6, 7]

if __name__ == '__main__':
    citations = [3,0,6,1,5] 
    print(Solution().hIndex(citations))


''' Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h
if h of his/her N papers have at least h citations each, and the other N − h
papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5] Output: 3  Explanation: [3,0,6,1,5] means the
researcher has 5 papers in total and each of them had               received
3, 0, 6, 1, 5 citations respectively.               Since the researcher has 3
papers with at least 3 citations each and the remaining               two with
no more than 3 citations each, her h-index is 3. Note: If there are several
possible values for h, the maximum one is taken as the h-index.
'''

