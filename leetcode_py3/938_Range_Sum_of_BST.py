# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def rangeSumBST(self, root, L, R):
		sum = 0
		if not root:
			return sum

		if L <= root.val <= R: # if current root val within range
			sum += root.val
			sum += self.rangeSumBST(root.left, L, R)
			sum += self.rangeSumBST(root.right, L, R)

		elif root.val < L: # current root val already smaller than L, so rest
							# of left subtree will be all smaller than range
							# therefore no need to go through left 

			sum +=	self.rangeSumBST(root.right, L, R) # go through right subtree

		elif root.val > R: # current root val already smaller than L, so rest
							# of right subtree will be all smaller than range
							# therefore no need to go through right 

			sum += self.rangeSumBST(root.left, L, R) # go through left subtree

		return sum



		

if __name__ == '__main__':

	root = [10,5,15,3,7,null,18]
	L = 7
	R = 15
	print(Solution().rangeSumBST(root, L, R))



'''  
Given the root node of a binary search tree, return the sum of values of
all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
'''

