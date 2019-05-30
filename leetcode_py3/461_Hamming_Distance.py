class Solution:
	def hammingDistance(self, x, y):
		if x < 0 or x >= 2**31 or y < 0 or y >= 2**31:
			return 

		else:
			bit_x = []
			bit_y = []

			if x == 0:
				bit_x.append(0)
			elif y == 0:
				bit_y.append(0)

			if x > y:
				while x/2 != 0:
					if x % 2 == 0:
						bit_x.insert(0, 0)
					else:
						bit_x.insert(0, 1)
					x = x // 2

					if y != 0:
						if y % 2 == 0:
							bit_y.insert(0, 0)
						else:
							bit_y.insert(0, 1)
						y = y // 2
					else:
						bit_y.insert(0, 0)
			else:
				while y/2 != 0:
					if y % 2 == 0:
						bit_y.insert(0, 0)
					else:
						bit_y.insert(0, 1)
					y = y // 2

					if x != 0:
						if x % 2 == 0:
							bit_x.insert(0, 0)
						else:
							bit_x.insert(0, 1)
						x = x // 2
					else:
						bit_x.insert(0, 0)
		return sum([1 for x, y in zip(bit_x, bit_y) if x != y])


if __name__ == '__main__':
	x = 1
	y = 4
	print(Solution().hammingDistance(x, y))
	i = 0
	j = 1
	print(Solution().hammingDistance(i, j))
