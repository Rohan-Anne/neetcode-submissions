# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        returnList = ListNode(0)
        newList = returnList
        while node1 or node2:
            # Check for empty nodes
            if not node1 and node2:
                newList.next = node2
                break
            elif not node2 and node1:
                newList.next = node1
                break
            elif not node1 and not node2:
                break
            
            # Maintain sorting invariant to construct new sorted list

            if node1.val <= node2.val:
                newList.next = ListNode(node1.val)
                node1 = node1.next
                newList = newList.next
            else:
                newList.next = ListNode(node2.val)
                node2 = node2.next
                newList = newList.next
            
            print(newList.val)
            
            

        
        return returnList.next

        