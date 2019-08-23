class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_water = 0
        
        while left <= right:
            base = right - left
            temp = base * min(height[right], height[left])
            max_water = max(max_water, temp)
            if height[left] < height[right]:
                left += 1   
            else:
                right -= 1
        return max_water


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))


''' 
Given n non-negative integers a1, a2, ..., an , where each represents a
point at coordinate (i, ai). n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most
water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this
case, the max area of water (blue section) the container can contain is 49.
'''
            
            