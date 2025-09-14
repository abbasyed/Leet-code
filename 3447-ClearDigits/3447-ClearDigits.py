# Last updated: 9/14/2025, 4:58:48 AM
class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
