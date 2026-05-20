class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []
        self.total=0
        def subsets(i):
            if self.total >= target or i >= len(nums):
                if self.total == target:
                    res.append(curr.copy())
                return

            curr.append(nums[i])
            self.total += nums[i]
            subsets(i)

            curr.pop()
            self.total -= nums[i]
            subsets(i+1)

        subsets(0)
        return res






        