class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        arr = [[] for _ in range(len(nums)+1)]

        for num in nums:
            if num in hash_map:
                hash_map[num] +=1
            else:
                hash_map[num] = 1

        for key in hash_map:
            arr[hash_map[key]].append(key)

        finalArr = []
        count = 0
        i = len(nums)
        while i >= 0:
            if len(arr[i]) != 0:
                g = 0
                while g < len(arr[i]):
                    finalArr.append(arr[i][g])
                    g+=1
                    count+=1
                    if (count == k):
                        return(finalArr)

            i -=1