class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * len(cost)

        first = cost[len(cost)-1]
        second = cost[len(cost)-2]
        arr[len(cost)-1] = first
        arr[len(cost)-2] = second


        for i in range(len(cost)-3, -1, -1):
            if first < second:
                arr[i] = first + cost[i]
            else: 
                arr[i] = second + cost[i]
            
            temp = second
            second = arr[i]
            first = temp

        if arr[0] < arr[1]: return arr[0]
        else: return arr[1]
        