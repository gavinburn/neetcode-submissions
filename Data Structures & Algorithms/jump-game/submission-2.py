from collections import defaultdict
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        currentIndex = 0
        currentOptions = defaultdict(int)

        while currentIndex < len(nums)-1:
            options = nums[currentIndex]
            if options == 0: return False
            for i in range (currentIndex + 1,currentIndex+options+1):
                if i < len(nums)-1:
                    currentOptions[i] = i + nums[i]
                else: 
                    print(i)
                    return True

            currentMax = 0
            newIndex = -1
            print(currentOptions)
            for key,value in currentOptions.items():
                if value>currentMax: 
                    currentMax=value
                    newIndex = key

            currentOptions.clear()
            currentIndex = newIndex

        return True       