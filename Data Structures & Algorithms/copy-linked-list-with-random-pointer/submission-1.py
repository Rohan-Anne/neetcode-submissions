"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # Create mapping of random pointers based on indexes
        oldNodes = dict()
        oldPointer = head
        count = 0
        while oldPointer:
            oldNodes[oldPointer] = count
            count += 1
            oldPointer = oldPointer.next
        mapping = dict()
        for pointer in oldNodes.keys():
            if pointer.random is not None:
                mapping[oldNodes[pointer]] = oldNodes[pointer.random]
            else:
                mapping[oldNodes[pointer]] = None
        
        # Create the new nodes
        storage = []
        curr = head
        while curr:
            temp = Node(curr.val, None, None)
            storage.append(temp)
            curr = curr.next

        # Attach the wires
        for i in range(len(storage)):
            if i != len(storage) - 1:
                storage[i].next = storage[i + 1]

            if mapping[i] is not None:
                storage[i].random = storage[mapping[i]]
    
        return storage[0]
        