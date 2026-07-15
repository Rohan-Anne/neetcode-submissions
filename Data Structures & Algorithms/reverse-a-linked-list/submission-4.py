# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prevElem = None
        currElem = head
        while currElem:
            temp = currElem.next
            currElem.next = prevElem
            prevElem = currElem
            currElem = temp
        return prevElem
        

            

        