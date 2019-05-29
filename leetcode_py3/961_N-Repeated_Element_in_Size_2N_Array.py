class Solution:
    def repeatedNTimes(self, A):
    	check_dict = {}
    	for num in A:
    		if num in check_dict:
    			return num
    		else:
    			check_dict[num] = 1

    def by_set(self, A):
    	check = set()
    	for num in A:
    		if num in check:
    			return num
    		else:
    			check.add(num)


if __name__ == "__main__":
	A = [1,2,3,3]
	print(Solution().repeatedNTimes(A))
	print(Solution().by_set(A))


'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
'''