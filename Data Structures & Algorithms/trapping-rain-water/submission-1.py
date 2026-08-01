class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0 
        heights = height
        right = len(heights)-1
        leftmax = heights[left]
        rightmax = height[right]

        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax = max(leftmax,heights[left])
                res+=leftmax-heights[left]
            else:
                right-=1
                rightmax = max(rightmax,heights[right])
                res+=rightmax-heights[right]
        return res