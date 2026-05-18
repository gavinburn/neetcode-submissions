class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1
        if n==2: return 2
        dpArray = [0] * n

        dpArray[0] =1
        dpArray[1]=2

        i=2

        while i < n:
            dpArray[i] = dpArray[i-1] + dpArray[i-2]
            i+=1

        return dpArray[n-1] 
        