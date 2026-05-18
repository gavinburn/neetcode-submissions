class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputArr=[]
        i=0
        while i < len(nums)-2:
            if i>0 and nums[i-1] == nums[i]:
                i+=1
                continue
            leftIndex=i+1
            rightIndex = len(nums) - 1

            while(leftIndex<rightIndex):
                sum = nums[i] + nums[leftIndex] + nums[rightIndex]
                if sum > 0:
                    rightIndex-=1
                elif sum < 0:
                    leftIndex+=1
                else:
                    outputArr.append([nums[i], nums[leftIndex], nums[rightIndex]])
                    leftIndex += 1
                    while leftIndex<rightIndex and nums[leftIndex] == nums[leftIndex-1]:
                        leftIndex += 1

            i+=1
        return outputArr