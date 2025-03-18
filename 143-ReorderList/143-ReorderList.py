# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        current = head

        # store all nodes in a nodes[] array
        while current:
            nodes.append(current)
            current = current.next

        l, r = 0, len(nodes)-1

        while l < r:
            # create connections in shuffling order
            nodes[l].next = nodes[r] 
            l += 1 

            if l < r:
                nodes[r].next = nodes[l] 
                r -= 1
        nodes[l].next = None

        