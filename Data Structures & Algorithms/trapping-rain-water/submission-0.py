class Solution:
    def trap(self, heights: List[int]) -> int:
        leftPointer=0
        rightPointer=len(heights)-1
        maxLeft=heights[leftPointer]
        maxRight=heights[rightPointer]
        rainWater=0
        for i, height in enumerate(heights):
            if maxLeft <= maxRight:
                water=maxLeft-heights[leftPointer]
                if heights[leftPointer] > maxLeft:
                    maxLeft=heights[leftPointer]
                leftPointer+=1
            else:
                water = maxRight - heights[rightPointer]
                if heights[rightPointer] > maxRight:
                    maxRight=heights[rightPointer]
                rightPointer -= 1
            if water < 0:
                water = 0
            rainWater += water

        return rainWater