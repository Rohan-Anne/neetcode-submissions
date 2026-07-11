# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 1
        while head:
            if head.val > 1000:
                return True
            head.val = 1000 + index
            index += 1
            head = head.next
        return False
        