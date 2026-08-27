class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        visited = set()
        count = 0

        for item in edges:
            node = item[0]
            neighbour = item[1]
            adjList[node].append(neighbour)
            adjList[neighbour].append(node)

        def recurse(node):
            if node in visited:
                return

            visited.add(node)
                
            for neighbour in adjList[node]:
                recurse(neighbour)

        for key in range(n):
            if key not in visited: count +=1   
            recurse(key) 

        return count   