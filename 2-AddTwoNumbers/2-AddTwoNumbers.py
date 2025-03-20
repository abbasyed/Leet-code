# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            # get x and y values for addition
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # do addition with carry
            total = x + y + carry
            carry = total // 10

            # add addition node to new list
            current.next = ListNode(total % 10)
            current = current.next

            # traverse through remaining nodes in l1 and l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # add carry if > 0
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next