class Solution:
    def sortArrayByParity(self, A)
        # odd_li = []
        # even_li = []
        # if len(A) >= 1 and len(A) <= 5000: 
        #     for element in A:
        #         if element >= 0 and element <= 5000:
        #             if element%2 == 0:
        #                 even_li.append(element)
        #             else:
        #                 odd_li.append(element)
        #     return even_li + odd_li

        return [x for x in A if x % 2==0] + [x for x in A if x % 2!=0]
            
if __name__ == '__main__':
    A = [3,1,2,4]
    print(sortArrayByParity(A))

'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''