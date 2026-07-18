"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            print("this ran")
            return node
        else:

            visited = {}


            def addToVisited(node):
                if node not in visited: 
                    visited[node] = ""
                else:
                    return
                for neighbour in node.neighbors:
                    addToVisited(neighbour)


            def makeConnections(node):
                if visited[node] == "":
                    visited[node] = Node(node.val, [])
                else:
                    return
                
                for neighbour in node.neighbors:
                    if visited[neighbour] != "":
                        visited[node].neighbors.append(visited[neighbour])
                    else:
                        makeConnections(neighbour)
                        visited[node].neighbors.append(visited[neighbour])

            addToVisited(node)
            makeConnections(node)
            return visited[node]





        