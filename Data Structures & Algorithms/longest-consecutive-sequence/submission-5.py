class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        longestStreak =1
        leftVals = []
        hash_set = set()
        for num in nums:
            hash_set.add(num)

        for num in hash_set:
            if num -1 not in hash_set:
                leftVals.append(num)

        index = 1;
        maxLongest = 1;
        for num in leftVals:
            while num + index in hash_set:
                index+=1
                longestStreak+=1;
            if(longestStreak>maxLongest):
                maxLongest = longestStreak
            longestStreak=1
            index=1
        return(maxLongest)