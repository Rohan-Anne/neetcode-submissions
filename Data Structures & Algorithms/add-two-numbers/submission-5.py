# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Count lengths of both lists and assign short and long list
        short = None
        long = None
        length1 = 0
        temp1 = l1
        while temp1.next is not None:
            length1 += 1
            temp1 = temp1.next
        length2 = 0
        temp2 = l2
        while temp2.next is not None:
            length2 += 1
            temp2 = temp2.next
        
        if length1 <= length2:
            short = l1
            long = l2
        else:
            short = l2
            long = l1
        
        # Add 2 numbers through iterative process
        addition = ListNode(None, None)
        temp = addition
        previousRemainder = False
        while short or long or previousRemainder:
            if short:
                summation = short.val + long.val
            elif short or long:
                summation = long.val
            else:
                summation = 0
            # Carry over remainder from earlier
            if previousRemainder:
                previousRemainder = False
                summation += 1
            # Do summation, accounting for remainder
            if summation > 9:
                previousRemainder = True
                summation -= 10
            temp.val = summation
            if long.next is None:
                break
            temp.next = ListNode(None, None)
            temp = temp.next
            # Go to next pointer in the short and long lists
            if short:
                short = short.next
            long = long.next
            
        if previousRemainder:
            temp.next = ListNode(1, None)
        return addition

        
        
    
            

        
        