class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax-height[r]
        return res