# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head=root
        recurse(root)
        return head


def recurse(root):
    if root:
        recurse(root.left)
        recurse(root.right)
        swap(root)
        

def swap(root):
    temp = root.left
    root.left = root.right
    root.right=temp

    
        