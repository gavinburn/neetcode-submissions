class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = []
        curr = []
        i=0

        def recurse(i):

            if i >= len(nums):
                item = curr.copy()
                output.append(item)
                return

            curr.append(nums[i])
            recurse(i+1)

            curr.pop()
            recurse(i+1)


        recurse(0)
        return output



            