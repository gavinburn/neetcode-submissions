# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxLevel=1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.recurse(root, 1)
            return self.maxLevel
        else: return 0
        

    def recurse(self, root, level):
        if root:
            if self.maxLevel < level:
                self.maxLevel=level
            self.recurse(root.left, level+1)
            self.recurse(root.right, level+1)


        

        