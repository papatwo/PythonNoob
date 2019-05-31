class Solution:
    def selfDividingNumbers(self, left, right):
        output = []
        for i in range(left, right+1):
            if '0' in str(i):
                continue
            else:
                check = []
            for ch_num in str(i):
                if i % int(ch_num) != 0:
                    check.append(0)
                else:
                    check.append(1)
            if 0 not in check:
                output.append(i)
        return output


if __name__ == '__main__':
    left = 1
    right = 22
    print(Solution().selfDividingNumbers(left, right))

''' 
A self-dividing number is a number that is divisible by every digit it
contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.

Example 1: Input:  left = 1, right = 22 Output: [1, 2, 3, 4, 5, 6, 7, 8, 9,
11, 12, 15, 22] Note:

The boundaries of each input argument are 1 <= left <= right <= 10000. '''
