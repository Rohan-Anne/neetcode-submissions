# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal, None, None)
        if len(preorder) == 1:
            return root 
        # Split inorder traversal
        leftIn = []
        rightIn = []
        currentIndex = None
        for i in range(len(inorder)):
            if inorder[i] != rootVal:
                leftIn.append(inorder[i])
            else:
                rightIn = inorder[i + 1:]
                break
        leftPre = preorder[1:len(leftIn) + 1]
        rightPre = preorder[len(leftIn) + 1:]

        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)
        return root
        
        