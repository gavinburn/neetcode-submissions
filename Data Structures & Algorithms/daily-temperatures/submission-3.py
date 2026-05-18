class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = deque()  
        for i, temp in enumerate(temperatures):  
            while stack and temperatures[stack[-1]] < temp:  
                prev_index = stack.pop()  
                res[prev_index] = i - prev_index  
            stack.append(i)  

        return res 