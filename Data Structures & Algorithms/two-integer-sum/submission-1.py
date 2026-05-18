class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        i=0
        stopCond = len(nums)
        while i < stopCond:
            offset = target - nums[i];
            if offset in myDict: return [myDict[offset], i]
            else:
                myDict[nums[i]] = i
                i+=1

        return []