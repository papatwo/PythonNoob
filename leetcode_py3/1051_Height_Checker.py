class Solution:
	def heightChecker(self, heights):
		count = 0
		sorted_heights = sorted(heights)
		for x, y in zip(sorted_heights, heights):
			if x != y: count += 1

		return count

	def by_list_compre(self, heights): 
		sorted_heights = sorted(heights)
		return sum([1 for x, y in zip(sorted_heights, heights) if x != y ])


if __name__ == '__main__':
	heights = [1,1,4,2,1,3]
	print(Solution().heightChecker(heights))
	print(Solution().by_list_compre(heights))


''' Students are asked to stand in non-decreasing order of heights for an
annual photo.

Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to be
standing in non-decreasing order of height.)

 

Example 1:

Input: [1,1,4,2,1,3] Output: 3 Explanation:  Students with heights 4, 3 and
the last 1 are not standing in the right positions. '''
