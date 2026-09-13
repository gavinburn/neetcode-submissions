class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArray = []
        maxVal = []
        val = 0


        for num in nums:
            newVal = val + num
            if newVal > 0: 
                val = newVal
                subArray.append(num)
                maxVal.append(val)
            else:
                val = 0
                subArray = []

        returnVal = -10000
        if len(maxVal) == 0:
            for val in nums:
                if val > returnVal: returnVal = val

            return returnVal

        for val in maxVal:
            if val > returnVal: returnVal = val

        return returnVal
