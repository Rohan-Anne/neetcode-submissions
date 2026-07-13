# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print("Current root value: " + str(root.val))
        lower, higher = p, q
        if q.val < p.val:
            lower, higher = q, p
        if lower.val <= root.val <= higher.val:
            return root
        if lower.val <= root.val and higher.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if lower.val > root.val and higher.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)



        
        

        



        