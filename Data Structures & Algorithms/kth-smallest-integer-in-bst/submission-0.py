# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTraversal(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return self.inOrderTraversal(root.left) + [root.val] + self.inOrderTraversal(root.right)

        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = self.inOrderTraversal(root)
        return inOrder[k - 1]
        
        

        