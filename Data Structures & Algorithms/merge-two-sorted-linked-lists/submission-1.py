# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        returnList = ListNode(0)
        newList = returnList
        while list1 or list2:
            # Check for empty nodes
            if not list1 and list2:
                newList.next = list2
                break
            elif not list2 and list1:
                newList.next = list1
                break
            elif not list1 and not list2:
                break
            
            # Maintain sorting invariant to construct new sorted list

            if list1.val <= list2.val:
                newList.next = ListNode(list1.val)
                list1 = list1.next
                newList = newList.next
            else:
                newList.next = ListNode(list2.val)
                list2 = list2.next
                newList = newList.next
            
            print(newList.val)
            
            

        
        return returnList.next

        