# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [(root, 0)]
        levels = []
        while len(queue) > 0:
            currentNode, currentLevel = queue.pop(0)
            if currentNode.left is not None:
                queue.append((currentNode.left, currentLevel + 1))
            if currentNode.right is not None:
                queue.append((currentNode.right, currentLevel + 1))
            while len(levels) < currentLevel + 1:
                levels.append([])
            levels[currentLevel].append(currentNode.val)
        return levels
        
        
        
        