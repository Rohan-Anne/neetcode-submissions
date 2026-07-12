# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: # No tree
            return 0
        elif root.left is None and root.right is None: # No children to connect to
            return 0
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.maxDepth(root.left) + self.maxDepth(root.right))
        

        