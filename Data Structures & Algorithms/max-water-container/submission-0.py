class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        leftPointer=0
        rightPointer=len(heights)-1

        while(leftPointer<rightPointer):
            if(heights[rightPointer]>=heights[leftPointer]):
                area = heights[leftPointer] * (rightPointer-leftPointer)
                leftPointer+=1
            else:
                area = heights[rightPointer] * (rightPointer - leftPointer)
                rightPointer-=1

            if area>maxArea: maxArea=area

        return maxArea