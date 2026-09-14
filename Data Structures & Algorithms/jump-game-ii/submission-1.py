class Solution:
    def jump(self, nums: List[int]) -> int:
        currentIndex = 0
        currentOptions = defaultdict(int)
        steps = 0


        while currentIndex < len(nums)-1:
            options = nums[currentIndex]
            print(options)
            for i in range (currentIndex + 1,currentIndex+options+1):
                if i <= len(nums)-1:
                    currentOptions[i] = i + nums[i]
                else:
                    break

            currentMax = 0
            newIndex = -1
            print(currentOptions)
            for key,value in currentOptions.items():
                
                if key == len(nums)-1:
                    ccurrentMax=value
                    newIndex = key
                    break
                if value>=currentMax: 
                    currentMax=value
                    newIndex = key
            
            print(newIndex)
            currentOptions.clear()
            currentIndex = newIndex
            steps +=1

        return steps       