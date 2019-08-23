class Solution:
    def trap(self, height):
        leftmost = 0
        rightmost = 0
        water = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            leftmost = max(leftmost, height[left])
            rightmost = max(rightmost, height[right])
            if leftmost < rightmost:
                water += leftmost - height[left]
                left += 1
            else:
                water += rightmost - height[right]
                right -= 1
        return water
        
if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))


''' 
Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it is able to trap after
raining. The above elevation map is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6
'''
