class Solution:
	def judgeCircle(self, moves):
		movement = {}

		movement['U'] = 1
		movement['D'] = -1
		movement['L'] = -1
		movement['R'] = 1

		position = [0, 0]
		for move in moves: 
			try:
				if move == 'U' or move == 'D':
					position[1] += movement[move]
				elif move == 'L' or move == 'R':
					position[0] += movement[move]
			except:
				print('Invalid movement!')

		if position == [0,0]:
			return True
		else:
			return False


	def method_2(self, moves):
		x = y = 0
		for move in moves:
			if move == 'U': 
				y += 1
			elif move == 'D': 
				y -= 1
			elif move == 'R': 
				x += 1
			elif move == 'L': 
				x -= 1

		return x == y == 0

	def fast_one_line(self, moves):
		return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')


if __name__ == '__main__':
	moves = "UD"
	print(Solution().judgeCircle(moves))
	print(Solution().method_2(moves))
	print(Solution().fast_one_line(moves))

''' There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
completes its moves.

The move sequence is represented by a string, and the character moves[i]
represents its ith move. Valid moves are R (right), L (left), U (up), and D
(down). If the robot returns to the origin after it finishes all of its moves,
return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make
the robot move to the right once, "L" will always make it move left, etc.
Also, assume that the magnitude of the robot's movement is the same for each
move.

Example 1:

Input: "UD" Output: true  Explanation: The robot moves up once, and then down
once. All moves have the same magnitude, so it ended up at the origin where it
started. Therefore, we return true. '''


