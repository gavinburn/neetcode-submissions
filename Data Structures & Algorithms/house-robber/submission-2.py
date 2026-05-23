class Solution:
    def rob(self, nums: List[int]) -> int:

        left = 0
        right = 1
        mx = 0

        if len(nums) < 3:
            if len(nums) < 2:
                return nums[0]
            else:
                return max(nums[1], nums[0])


        nums[1] = max(nums[0], nums[1])  # add this

        for i in range(2, len(nums), 1):
            if nums[left] + nums[i] > nums[right]:
                nums[i]= nums[left] + nums[i]
            else: 
                nums[i] = nums[right]
            
            left+=1
            right +=1

        return nums[-1]



        