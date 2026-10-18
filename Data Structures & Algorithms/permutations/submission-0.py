class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        workingSet = set()

        curr = []
        output = []


        def recurse(curr):

            if len(nums) == len(curr):
                output.append(curr.copy())
                return

            for num in nums:
                if num not in workingSet:
                    curr.append(num)
                    workingSet.add(num)
                    recurse(curr)
                    curr.remove(num)
                    workingSet.remove(num)
        


        recurse(curr)
        return output
