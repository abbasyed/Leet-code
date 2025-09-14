# Last updated: 9/14/2025, 4:58:54 AM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        for p, s in pair:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)