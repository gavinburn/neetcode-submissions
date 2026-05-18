class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = []
        currentPref = 1;
        count =0;
        while count < len(nums):
            if(count != 0):
                currentPref *=nums[count-1]
            count +=1
            prefixArr.append(currentPref)

        count-=1;
        currentSuf = 1;
        suffixArr = []
        while count >= 0:
            if count != (len(nums) - 1):
                currentSuf *= nums[count+1]

            count-=1
            suffixArr.insert(0,currentSuf)

        while count < len(nums):
            nums[count] = prefixArr[count] * suffixArr[count]
            count+=1

        return(nums)