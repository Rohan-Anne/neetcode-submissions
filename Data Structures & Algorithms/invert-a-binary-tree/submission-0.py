# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if root is None:
            return None
        # perform switch
        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        # Recurse on tree children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


        
        