class Solution:
    def peakIndexInMountainArray(self, A):
        mid = len(A)//2
        L = len(A)
        # print(mid)
        # print(A[0:mid+1])
        # print(A[mid-1:L+1])
        while A[0:mid+1] != sorted(A[0:mid+1]) or A[mid:L+1] != sorted(A[mid:L+1],reverse=True):
            if A[mid] < A[mid-1]:
                mid -=1
            elif A[mid] < A[mid+1]:
                mid +=1
        return mid



    def binary_search(self, A):
        mid = len(A)//2
        low = 0
        high = len(A) - 1
        while low < high:
            if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
                return mid
            elif A[mid-1] < A[mid] < A[mid+1]:
                low = mid
            elif A[mid-1] > A[mid] > A[mid+1]:
                high = mid
            mid = (low + high) // 2

if __name__ == '__main__':
    A = [0,2,1,0]
    print(Solution().peakIndexInMountainArray(A))
    print(Solution().binary_search(A))

# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1



