# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    stack = []
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root:
            print(self.isAncestor(root, p, q, 0))
            if self.isAncestor(root,p,q,0) == 2:
                self.stack.append(root)
            self.lowestCommonAncestor(root.left, p, q)
            self.lowestCommonAncestor(root.right, p, q)
            
        if self.stack: return self.stack[-1]
        return None
        

    def isAncestor(self, root, p, q, found) -> int:
        if root:
            if root.val is p.val or root.val is q.val:
                found += 1
            found+=self.isAncestor(root.left, p, q, 0)
            found+=self.isAncestor(root.right, p, q, 0)
            return found
        return 0