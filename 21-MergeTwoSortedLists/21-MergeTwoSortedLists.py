# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #create a dummy head
        dummy = ListNode(-1)
        
        # keep track of the tail of our merged list
        tail = dummy

        # iterate while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                # take from list1
                tail.next = list1
                list1 = list1.next
            else:
                # take from list2
                tail.next = list2
                list2 = list2.next
            # Move tail pointer forward
            tail = tail.next
            
        # attach any remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next