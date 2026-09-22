class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = set()

        def recurse(nums):

            if tuple(nums) not in output:
                output.add(tuple(nums))
            if len(nums) == 0:
                return

            for i in range(len(nums)):
                newNums = nums.copy()
                newNums.pop(i)

                recurse(newNums)

        recurse(nums)

        outArr = []

        for item in output:
            outArr.append(list(item))

        return outArr
