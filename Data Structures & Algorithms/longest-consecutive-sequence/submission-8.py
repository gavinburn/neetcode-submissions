class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0): return 0
        maxLongest = 1
        longestStreak =1
        hash_set = set()
        for num in nums:
            hash_set.add(num)

        for num in hash_set:
            if num -1 not in hash_set:
                while num + longestStreak in hash_set:
                    longestStreak += 1;
                if (longestStreak > maxLongest):
                    maxLongest = longestStreak
                longestStreak = 1
        return maxLongest