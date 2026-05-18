# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    same = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            if root.val == subRoot.val:
                self.same=True
                self.recurseBoth(root, subRoot)

                if self.same: return True
            
            self.isSubtree(root.left, subRoot)
            self.isSubtree(root.right, subRoot)
        return self.same

    def recurseBoth(self, leftRoot, rightRoot):

        if leftRoot and rightRoot:
            if leftRoot.val != rightRoot.val: self.same = False
            self.recurseBoth(leftRoot.left, rightRoot.left)
            self.recurseBoth(leftRoot.right, rightRoot.right)


        elif leftRoot or rightRoot:
            self.same=False
            
    



            

        