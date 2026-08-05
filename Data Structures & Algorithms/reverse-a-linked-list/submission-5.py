# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        temp = head
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        temp.next = self.reverseList(head)
        return temp

        

        