class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while r > l:
            currentArea = min(heights[l], heights[r]) * (r-l)
            maxArea = max(currentArea, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return maxArea