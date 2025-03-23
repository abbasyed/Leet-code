# Last updated: 3/23/2025, 2:50:18 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return 1

        prev1 = 1
        prev2 = 1

        for i in range(2, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return prev2