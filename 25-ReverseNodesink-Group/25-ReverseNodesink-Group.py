# Last updated: 4/8/2025, 12:23:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head
        
        prev = None
        curr = head
        for i in range(k):
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        head.next = self.reverseKGroup(curr, k)

        return prev