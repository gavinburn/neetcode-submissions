class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0] = 1
        postfix[len(nums)-1]=1

        i=0
        count1=1
        count2=1
        while i < len(nums)-1:
            count1 *= nums[i]
            prefix[i+1]=count1
            i+=1
        while i >= 1:
            count2 *= nums[i]
            postfix[i-1] = count2
            i -= 1

        outputArr = [0] * len(nums)
        k=0
        while k < len(nums):
            outputArr[k] = prefix[k]*postfix[k]
            k+=1

        return outputArr