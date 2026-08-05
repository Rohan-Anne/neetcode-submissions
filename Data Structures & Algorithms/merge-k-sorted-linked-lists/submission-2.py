# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def traversal(self, node):
        if node is None:
            return
        if node.next is None:
            print([node.val])
        array = [node.val]
        node = node.next
        while node is not None:
            array.append(node.val)
            node = node.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode(None, None)
        start = node
        merged = node
        while len(lists) > 0:
            #self.traversal(start)
            #print("Lists before manipulation: " + str(lists))
            minValue = None
            minNodeIndex = None
            for i in range(len(lists)):
                if lists[i] is not None:
                    if minValue is None:
                        minValue = lists[i].val
                        minNodeIndex = i
                    elif lists[i].val < minValue:
                        minValue = lists[i].val
                        minNodeIndex = i
            #print("Min value " + str(minValue))
            #print("Min Node: " + str(minNodeIndex))
            temp = lists[minNodeIndex]
            lists[minNodeIndex] = lists[minNodeIndex].next
            if lists[minNodeIndex] is None:
                lists.pop(minNodeIndex)
            if len(lists) > 0:
                temp.next = ListNode(None, None)
            merged.next = temp
            merged = merged.next
            #print("Lists after manipulation: " + str(lists))
        
        return start.next
                
        

        