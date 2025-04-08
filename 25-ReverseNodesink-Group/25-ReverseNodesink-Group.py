# Last updated: 4/8/2025, 12:25:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # count the values in the nodes
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        # if count is less than k return head
        if count < k:
            return head
        
        # reverse the nodes by using prev and curr pointers
        prev = None
        curr = head
        for i in range(k):
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        # connect remaining nodes by recursive call
        head.next = self.reverseKGroup(curr, k)

        # return the result
        return prev