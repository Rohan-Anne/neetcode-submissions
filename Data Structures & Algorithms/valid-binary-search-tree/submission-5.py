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
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = self.inOrderTraversal(root)
        if len(inOrder) < 2:
            return True
        previousVal = inOrder[0]
        for i in range(1, len(inOrder)):
            if inOrder[i] <= previousVal:
                return False
            previousVal = inOrder[i]
        return True
        