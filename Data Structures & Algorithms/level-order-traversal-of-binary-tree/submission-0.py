# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
                if not root:
                    return []

                result = []
                queue = deque([root])  # start with root in queue

                while queue:
                    level = []
                    n=len(queue)
                    i=0
                    while i<n:
                        node = queue.popleft()  # pop from front
                        level.append(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                        i+=1

                    result.append(level)

                return result