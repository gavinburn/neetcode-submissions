# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    valid = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.checker(root, 100000, -100000)
        return self.valid

    def checker(self, root, max, min):
        if root:
            if root.val <= min or root.val >= max:
                self.valid = False 
            if min != 0:
                self.checker(root.left, root.val, min)
            else:
                self.checker(root.left, root.val, 0)

            if max != 0:
                self.checker(root.right, max, root.val)
            else: 
                self.checker(root.right, 0, root.val)
            
