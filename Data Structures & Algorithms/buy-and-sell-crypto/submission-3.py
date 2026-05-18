class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            day1=0
            sellday=1
            maxPrice =0
            while sellday < len(prices):
                if prices[sellday] < prices[day1]:
                    day1 = sellday
                else:
                    if prices[sellday] - prices[day1] > maxPrice: maxPrice = prices[sellday] - prices[day1]
                sellday+=1
            return maxPrice