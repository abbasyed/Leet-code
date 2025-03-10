# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """Initially:
            NULL <- 1 -> 2 -> 3 -> 4 -> 5 -> NULL
            prev  curr  next

        After first iteration:
        NULL <- 1    2 -> 3 -> 4 -> 5 -> NULL
                prev  curr  next

        After second iteration:
        NULL <- 1 <- 2    3 -> 4 -> 5 -> NULL
                    prev  curr  next

... and so on until current becomes NULL"""

        prev = None
        curr = head

        while curr:
            # Store next node before we change current.next
            next_tmp = curr.next
            # Reverse the link
            curr.next = prev
            # Move pointers one position ahead
            prev = curr
            curr = next_tmp

        return prev