# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    same = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.recurseBoth(p,q)
        return self.same

    
    def recurseBoth(self, leftRoot, rightRoot):

        if leftRoot and rightRoot:
            if leftRoot.val != rightRoot.val: self.same = False
            self.recurseBoth(leftRoot.left, rightRoot.left)
            self.recurseBoth(leftRoot.right, rightRoot.right)


        elif leftRoot or rightRoot:
            self.same=False


        

        