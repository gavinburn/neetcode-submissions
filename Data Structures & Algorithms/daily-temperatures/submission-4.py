class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            solArray = [0] * len(temperatures)
            stack= deque()
            i=0

            for i, temp in enumerate(temperatures):
                while stack and temp>temperatures[stack[-1]]:
                    top=stack[-1]
                    solArray[top] = i - top
                    stack.pop()
                stack.append(i)



            return solArray
