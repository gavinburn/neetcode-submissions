class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        curr = []
        output = []
        level = 0
        workingSet = set()

        def recurse(curr, level):

            if level >= len(nums):
                if tuple(sorted(curr)) not in workingSet:
                    output.append(curr.copy())
                    workingSet.add(tuple(sorted(curr)))
                return

            curr.append(nums[level])
            level += 1


            recurse(curr, level)

            curr.pop()
            recurse(curr,level)     


        recurse(curr, level)
        return output       