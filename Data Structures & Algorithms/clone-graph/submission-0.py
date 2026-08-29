"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraphHelper(self, node, seen, mapping):
        if node is None:
            return None
        if node.val not in seen:
            root = Node(node.val)
            seen.add(node.val)
            mapping[node.val] = root
            for neighbor in node.neighbors:
                finalizedNeighbor = self.cloneGraphHelper(neighbor, seen, mapping)
                root.neighbors.append(finalizedNeighbor)
            print(root.val)
            print(root.neighbors)
            return root
        else:
            return mapping[node.val]
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = set()
        mapping = dict()
        return self.cloneGraphHelper(node, seen, mapping)
        