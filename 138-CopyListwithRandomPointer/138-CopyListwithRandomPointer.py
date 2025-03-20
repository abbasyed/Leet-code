"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if empty return None
        if not head:
            return None

        toCopy = {}

        # copy all the Nodes to toCopy{} hashmap
        current = head
        while current:
            toCopy[current] = Node(current.val)
            current = current.next
        
        # connect Next and Random Pointers
        current = head
        while current:
            if current.next:
                toCopy[current].next = toCopy[current.next]
            
            if current.random:
                toCopy[current].random = toCopy[current.random]

            current = current.next
        
        return toCopy[head]