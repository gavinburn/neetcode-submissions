class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        outputArr = []
        for i, num in enumerate(nums):
            l=i+1
            k = len(nums)-1
            if i != 0 and nums[i]==nums[i-1]:continue
            while k>l:
                if nums[i]+nums[k]+nums[l] == 0:
                    outputArr.append([nums[i],nums[l],nums[k]])
                    l+=1
                    while k>l and nums[l] == nums[l-1]:
                        l+=1
                elif nums[i]+nums[k]+nums[l] > 0: k-=1
                else: l+=1


        return outputArr