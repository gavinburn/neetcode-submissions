class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        curr = []
        output = []
        level = 0

        def recurse(curr, level):

            if level >= len(nums):
                print(curr)
                output.append(curr.copy())
                return

            curr.append(nums[level])
            level += 1

            recurse(curr, level)

            curr.pop()
            recurse(curr,level)     


        recurse(curr, level)
        return output       



        