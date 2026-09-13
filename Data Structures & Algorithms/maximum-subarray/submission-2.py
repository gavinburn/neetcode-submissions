class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArray = []
        currentMax = 0
        val = 0


        for num in nums:
            newVal = val + num
            if newVal > 0: 
                val = newVal
                subArray.append(num)
                if val > currentMax: currentMax = val
            else:
                val = 0
                subArray = []

        returnVal = -10000
        if currentMax == 0:
            for val in nums:
                if val > returnVal: returnVal = val

            return returnVal

        else: return currentMax
