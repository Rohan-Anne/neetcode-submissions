# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First, we find the length of the list
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        forwardIndex = (length - n) + 1
        # Set up iteration

        previousNode = None
        currentNode = head
        nextNode = head.next

        while currentNode:
            forwardIndex -= 1
            if forwardIndex == 0:
                if previousNode is None:
                    if head == currentNode:
                        currentNode = currentNode.next
                        head = currentNode
                    else:
                        currentNode = currentNode.next

                else:
                    previousNode.next = currentNode.next
                break

            previousNode = currentNode
            currentNode = currentNode.next
            
        return head

        








            
            
        