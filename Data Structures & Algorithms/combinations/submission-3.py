class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        start = []
        output = []
        curr=[]

        for i in range(1, n + 1):
            start.append(i)

        def recurse(i):
            if len(curr) >= k:
                item = curr.copy()
                output.append(item)
                return
            if i >= len(start):
                return

            curr.append(start[i])
            recurse(i+1)

            curr.pop()
            recurse(i+1)


        recurse(0)
        return output