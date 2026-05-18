class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer=0
        rightPointer=1
        maxGain=0
        while leftPointer<len(prices) and rightPointer<len(prices):
            gain = prices[rightPointer] - prices[leftPointer]
            if gain<0:
                leftPointer+=1
            else:
                if gain>maxGain: maxGain=gain
                rightPointer+=1

        return maxGain