class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000]*(amount+1)

        dp[0] = 0

        for num in range(1, amount+1):
            for coin in coins:
                if num >= coin:
                    dp[num] = min(dp[num], 1+dp[num-coin])


        for item in dp:
            print(item)


        if dp[amount] == 10000: return -1
        else: return dp[amount]