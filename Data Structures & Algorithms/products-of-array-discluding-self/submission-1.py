class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArr = [1] * len(nums)
        currentPref = 1;
        count =0;
        while count < len(nums):
            if(count != 0):
                currentPref *=nums[count-1]
            outputArr[count] = (currentPref)
            count +=1

        count-=1;
        currentSuf = 1;
        while count >= 0:
            if count != (len(nums) - 1):
                currentSuf *= nums[count+1]

            outputArr[count] *=currentSuf
            count-=1

        return(outputArr)