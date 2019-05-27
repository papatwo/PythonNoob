class Solution:
	def numJewelsInStones(self, J, S):
		stone_dict = {}
		for j in J:
			stone_dict[j] = 0

		for s in S:
			if s in stone_dict.keys():
				stone_dict[s] += 1

		return sum(stone_dict.values())


	def even_simpler(self, J, S):
		J_count = 0
		for s in S:
			J_count += s in J

		return J_count



if __name__ == '__main__':
	J = "aA"
	S = "aAAbbbb"
	print(Solution().numJewelsInStones(J, S))
	print(Solution().even_simpler(J, S))


''' 
You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.  Each character in S is a type of
stone you have.  You want to know how many of the stones you have are also
jewels.

The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb" Output: 3 

Example 2:

Input: J = "z", S = "ZZ" Output: 0 
'''

