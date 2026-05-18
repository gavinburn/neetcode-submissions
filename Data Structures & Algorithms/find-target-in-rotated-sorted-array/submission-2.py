class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right = len(nums)-1
        while left < right:
            middle = (right + left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else: right = middle

        middle = left

        left=0
        right=len(nums)-1
        if (target > nums[right]):
            right = middle-1
        elif target < nums[right]:
            left = middle
        else: return right

        while left < right:
            middle = (right + left) // 2
            if (target>nums[middle]):
                left = middle +1
            elif target < nums[middle]:
                right = middle-1
            else:
                left = middle
                right=left

        if nums[left] != target: left = -1
        return left