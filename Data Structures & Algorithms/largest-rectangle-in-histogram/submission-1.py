class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        maxLen = len(heights)
        newIndex=0
        changed = False;
        for i,height in enumerate(heights):
            while(stack and stack[-1][0] > height):
                changed=True
                poppedObj = stack.pop()
                newIndex = poppedObj[1]
                if ((i-poppedObj[1]) * poppedObj[0])>maxArea: maxArea=((i-poppedObj[1]) * poppedObj[0])

            if changed:
                stack.append((height, newIndex))
                changed=False

            else: stack.append((height, i))

        for pairs in stack:
            if ((maxLen - pairs[1]) * pairs[0]) > maxArea: maxArea = ((maxLen - pairs[1]) * pairs[0])

        return maxArea