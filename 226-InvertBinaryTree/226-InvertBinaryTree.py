# Last updated: 4/9/2025, 10:45:13 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # base condition:
        if not root:
            return None
        
        # swap nodes:
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursive call for remaining nodes:
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Time Complexity: O(n) where n is the number of nodes in the tree We visit each node exactly once

# Space Complexity: O(h) where h is the height of the tree
# The recursion stack will at most contain h function calls
# In the worst case (a skewed tree), h = n, making it O(n)
# In the best case (a balanced tree), h = log(n), making it O(log n)