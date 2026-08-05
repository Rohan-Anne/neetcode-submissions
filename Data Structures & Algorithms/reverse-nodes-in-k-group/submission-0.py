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
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        temp = head
        tempK = k - 1
        while temp.next and tempK > 0:
            temp = temp.next
            tempK -= 1
        # Option 1: Current list doesnt have k nodes
        if tempK > 0:
            return head
        # Option 2: Current list has k nodes
        else:
            # Separate k nodes from rest of list
            remaining = temp.next
            temp.next = None
            # Reverse k nodes
            reverse = self.reverseList(head)
            traversal = reverse
            while traversal.next:
                traversal = traversal.next
            traversal.next = self.reverseKGroup(remaining, k)
            return reverse
            
        

        