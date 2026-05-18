class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        index = 0

        for num in nums:
            offset = target - num
            if offset in hash_map:
                return([hash_map[offset], index])
            else:
                hash_map[num] = index

            index = index + 1