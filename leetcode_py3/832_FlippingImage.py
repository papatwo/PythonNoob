class Solution:
	def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
		# invert_A = []
		# inverse_A = [row[::-1] for row in A]
		# for row in inverse_A:
		#     invert = [x+1 if x==0 else x-1 for x in row]
		#     invert_A.append(invert)
		# return invert_A

		inverse_A = [[1-x for x in row[::-1]] for row in A]
		return inverse_A

if __name__ == '__main__':
	A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
	print(Solution().flipAndInvertImage(A))

'''
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
'''