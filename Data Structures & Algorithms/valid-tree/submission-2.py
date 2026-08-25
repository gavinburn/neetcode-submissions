class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visited = set()

        for item in edges:
            node = item[0]
            neighbour = item[1]
            adjList[node].append(neighbour)
            adjList[neighbour].append(node)

        def recurse(node, previous):
            if node in visited:
                return False

            visited.add(node)
                
            for neighbour in adjList[node]:
                if neighbour != previous:
                    if recurse(neighbour, node) is False: return False

            return True

        if recurse(0, None) and len(visited) == n: return True
        else: return False        