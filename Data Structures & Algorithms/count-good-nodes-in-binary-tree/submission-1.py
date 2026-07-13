# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def goodNodes(self, root: TreeNode) -> int:
        countGoodNodes = 0
        queue = [(root, root.val)]
        while len(queue) > 0:
            currentNode, currentVal = queue.pop(0)
            if currentNode.val >= currentVal:
                currentVal = currentNode.val
                countGoodNodes += 1
            if currentNode.left is not None:
                queue.append((currentNode.left, currentVal))
            if currentNode.right is not None:
                queue.append((currentNode.right, currentVal))
        return countGoodNodes


        