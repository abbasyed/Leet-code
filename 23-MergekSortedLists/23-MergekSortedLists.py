# Last updated: 4/8/2025, 11:55:36 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # base condition:
        if not lists:
            return None

        heap = []
        dummy = ListNode(0)
        current = dummy

        #add first three nodes from lists to heap
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap,(head.val, i, head))

        #process remaining nodes and result
        while heap:
            val, i, node = heapq.heappop(heap)
            #create a node connection
            current.next = node
            current = current.next
            
            #push remaining nodes into heap
            if node.next:
                heapq.heappush(heap,(node.next.val, i, node.next))
        
        return dummy.next